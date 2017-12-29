

from sanic import response

from functools import wraps
import re  #正则表达式判断模块

from app.pg import pg

#验证手机号码是否正确
def phone(phone):
    val = re.match('^1\d{10}$',phone)
    if val:
        return True
    return False


#检验密码格式是否正确
def password(password):
    val = re.match('^(?=.*\d)(?=.*[a-zA-Z])(?!.*\s).{8,16}$',password)
    if val:
        return True
    return False

# 检查token
def token_check(func):
    @wraps(func)
    def wrapper(request,*args, **kwargs):
            #判断是否有token
            try:
                value =request.headers['token']
            except KeyError:
                return response.json({"msg_code":"0555","message":"please add token"})
            #以token为key取value
            if not len(value)==32:
                return response.json({"msg_code":"0555","message":"token error"})
            redis_cli =redis.get_redis_client()
            uid =redis_cli.get(value)
            if not uid:
                return response.json({"msg_code":"0555","message":"token expired"})
            request.form['user_id'] = [uid.decode()]
            #刷新key有效期
            redis_cli.expire(value,3600*72)
            return func(request,*args, **kwargs)
    return wrapper


def token_check_one(func):
    @wraps(func)
    def wrapper(request,*args, **kwargs):
            #判断是否有token
            try:
                value =request.headers['token']
            except KeyError:
                return response.json({"msg_code":"0555","message":"please add token"})
            #以token为key取value
            if not len(value)==32:
                return response.json({"msg_code":"0555","message":"token error"})
            
            datapool = await pg.setup_connection()
            
            redis_cli =redis.get_redis_client()
            uid =redis_cli.get(value)
            if not uid:
                return response.json({"msg_code":"0555","message":"token expired"})
            request.form['user_id'] = [uid.decode()]
            #刷新key有效期
            redis_cli.expire(value,3600*72)
            return func(request,*args, **kwargs)
    return wrapper