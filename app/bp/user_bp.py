import uuid
import json

from sanic import Blueprint,response

from app.exceptions import  app_exception


from utils import MD5_util,response_util,data_util

# from config import settings

user_bp=Blueprint('user_bp',url_prefix='/user')


@user_bp.post('/login')
async def login(request):
    data = request.json
    try :
        data['username']
        data['pwd']
    except KeyError as e:
        raise app_exception.params_error(str(e)+'is empty or wrong')
    async with user_bp.pool.acquire( ) as conn:
        stmt = await conn.prepare('''select * from "user" WHERE username = $1''')
        user = dict(await stmt.fetchrow(data['username']))
    if not user:
        raise app_exception.data_no_exit_error(data['username']+ '没有注册')
    #TODO rsa解密
    if not MD5_util.md5Encode(str(data['pwd']))==user['pwd']:
        print(MD5_util.md5Encode(str(data['pwd'])))
        raise app_exception.data_error('密码错误')
    user.pop('pwd')
    #设置token
    try:
        token = str(uuid.uuid4()).replace('-', '')
    except Exception:
        raise app_exception.data_error('set token fail')
    async with user_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''update "user" set token = $1 WHERE id = $2''')
        await stmt.fetchrow(token,user['id'])
    return response.json(response_util.success(user =user))

@user_bp.post('/edit_phone')
async def edit_phone(request):
    user=await  data_util.token(request,1)
    if user==False:
        return response.json({"status":"002","message":"no permission"})
    data = request.json
    user_id = user['id']
    async with user_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''update "user" set phone = $1 WHERE id = $2''')
        await stmt.fetchrow(data['phone'],user_id)
    return response.json({"status": "succeed"})



@user_bp.post('/edit_pwd')
async def edit_pwd(request):
    user = await  data_util.token(request, 1)
    if user == False:
        return response.json({"status": "002", "message": "no permission"})

    data=request.json
    user_id = user['id']
    async with user_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''select * from "user" WHERE id = $1''')
        user = dict(await stmt.fetchrow(user_id))
    newPwd = MD5_util.md5Encode(str(data['pwd']))
    print(MD5_util.md5Encode("aaa"))
    if not newPwd==user['pwd']:
        raise app_exception.data_error('密码错误')
    async with user_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''update  "user" set pwd = $1 WHERE id = $2''')
        await stmt.fetchrow(MD5_util.md5Encode(data['new_pwd']),user_id)
    return response.json({"status": "succeed"})

@user_bp.post('/add_user')
async def add_user(request):
    user = await  data_util.token(request, 2)
    if user == False:
        return response.json({"status": "002", "message": "no permission"})


    data = request.json
    try :
        data['username']
        data['pwd']
        data['phone']
    except KeyError as e:
        raise app_exception.params_error(str(e)+'is empty or wrong')

    newPwd = MD5_util.md5Encode(str(data['pwd']))
    async with user_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''insert into  "user" (username,pwd,phone,lv) values ($1,$2,$3,1) ''')
        await stmt.fetchrow(data['username'],newPwd,data['phone'])
    return response.json({"status": "succeed"})


@user_bp.post('/add_user_two')
async def add_user_two(request):
    data = request.json        
    try :
        data['username']
        data['pwd']
        data['phone']
    except KeyError as e:
        raise app_exception.params_error(str(e)+'is empty or wrong')

    newPwd = MD5_util.md5Encode(str(data['pwd']))
    async with user_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''insert into  "user" (username,pwd,phone,lv) values ($1,$2,$3,2) ''')
        await stmt.fetchrow(data['username'],newPwd,data['phone'])
    return response.json({"status": "succeed"})




# @user_bp.post('/logout')
# @data_util.token_check
# async def logout(request):
#     token=request.headers['token']
#     redis.get_redis_client().delete(token)
#     return response.json(response_util.success())

# @user_bp.post('/update_info')
# @data_util.token_check
# async def update_info(request):
#     user_id=request.form.get('user_id')
#     # {"nickname":"xxx",
#     #  "sex":"",
#     #  "avater":"xxx"
#     #
#     # }

# @user_bp.post('/add_star')   #form提交
# @data_util.token_check
# async def add_star(request):
#     user_id =  uuid.UUID(str(request.form.get('user_id')))
#     try:
#         share_id = uuid.UUID(str(request.form.get('share_id')))
#     except KeyError as e:
#         raise app_exception.params_error(str(e)+'is empty or wrong')
#     if await add(share_id,user_id):
#         return response.json(response_util.success('success'))
#     else:
#         raise app_exception.data_error('您已收藏过该分享')




# async def add(id,user_id):
#     async with user_bp.pool.acquire() as conn:
#         stmt = await conn.prepare('''select star  from "user" WHERE id = $1''')
#         value =await stmt.fetchrow(user_id)
#     value = dict(value)['star']
#     if value==None:
#         value=[]
#     if id in value:
#         return False
#     else:
#         value.append(id)

#         try:
#             async with user_bp.pool.acquire() as conn:
#                 stmt = await conn.prepare('''update "user" set star = $1 WHERE id = $2''')
#                 await stmt.fetchrow(value,user_id)
#         except Exception as e:
#             print(e)
#             raise app_exception.data_error('add fail')
#     return True


# @user_bp.post('/del_star')   #form提交
# @data_util.token_check
# async def del_star(request):
#     user_id = str(request.form.get('user_id'))
#     user_id =uuid.UUID(user_id)
#     try:
#         share_id = uuid.UUID(str(request.form.get('share_id')))
#     except KeyError as e:
#         raise app_exception.params_error(str(e) + 'is empty or wrong')
#     if await dele(share_id, user_id):
#         return response.json(response_util.success('success'))
#     else:
#         raise app_exception.data_error('您未收藏过该分享')

# async def dele(id,user_id):
#     async with user_bp.pool.acquire() as conn:
#         stmt = await conn.prepare('''select star  from "user" WHERE id = $1''')
#         value = await stmt.fetchrow(user_id)
#     value = dict(value)['star']
#     if value==None:
#         raise app_exception.data_error('no satr')
#     if id not in value:
#         return False
#     else:
#         value.remove(id)
#         if len(value)==0:
#             value=None

#         try:
#             async with user_bp.pool.acquire() as conn:
#                 stmt = await conn.prepare('''update "user" set star = $1 WHERE id = $2''')
#                 await stmt.fetchrow(value,user_id)
#         except Exception as e:
#             print(e)
#             raise app_exception.data_error('del fail')
#     return True


# @user_bp.get('/get_star/<page:int>')   #form提交
# @data_util.token_check
# async def get_star(request,page):
#     user_id = str(request.form.get('user_id'))
#     async with user_bp.pool.acquire() as conn:
#         stmt = await conn.prepare('''select star->'star' from "user" WHERE id = $1''')
#         value = await stmt.fetchrow(user_id)
#         # print(dict(value)['?column?'])->[{"id":1},{"id":2}]
#     value = json.loads(dict(value)['?column?'])
#     if value == None:
#         raise app_exception.data_error('no satr')
#     value.reverse()
#     start_page = (page-1)*settings.page_num
#     value = value[start_page:start_page+settings.page_num]
#     it = iter(value)
#     for x in it:
#         async with user_bp.pool.acquire() as conn:
#             stmt = await conn.prepare('''select title, from "user" WHERE id = $1''')
