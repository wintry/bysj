# -*- coding: utf-8 -*-

# from config import redis
import json

class appexception(Exception):
    status_code = 200

    def __init__(self, message, mess_code=None):
        super().__init__(self)
        self.message = message
        if mess_code is not None:
            self.mess_code = mess_code

    def to_dict(self):
        rv = dict({})
        rv['message'] = self.message
        rv['msg_code'] =self.mess_code
        return json.dumps(rv)

class params_error(appexception):
    mess_code = '0400'

class data_no_exit_error(appexception):
    mess_code = '0401'

class data_error(appexception):
    mess_code = '0402'



# #定义防爬方法
# def security(ip,path):
#     '''3秒钟不能超过２０次请求，否则返回Ｆalse'''
#     key ='security'+ip
#     redis_client =redis.get_redis_client()
#     count =redis_client.hget(key,path);
#     if count:
#         count =int(count)
#         if count<40:
#             redis_client.hset(key,path,count+1)
#         else:
#             return False
#     else:
#         redis_client.hset(key,path,'1')
#         redis_client.expire(key,5)
#     return True

