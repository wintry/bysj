import uuid
import json

from sanic import Blueprint,response

from app.exceptions import  app_exception


from utils import MD5_util,response_util,data_util

# from config import settings

logs_bp=Blueprint('logs_bp',url_prefix='/logs')


@logs_bp.post('/add_log')
async def add_log(request):
    user = await  data_util.token(request, 1)
    if user == False:
        return response.json({"status": "002", "message": "no permission"})

    data = request.json


    async with logs_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''insert into  "logs" (content, user_id, create_time) values ($1,$2,$3) ''')
        await stmt.fetchrow(data['content'],user['id'],data['time'])
    return response.json({"status": "succeed"})

@logs_bp.get('/get_logs')
async def getlog(request):
    user = await  data_util.token(request, 1)
    if user == False:
        return response.json({"status": "002", "message": "no permission"})
    async with logs_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''select * from "logs" ORDER BY id DESC ''')
        bugs = await stmt.fetch()
    bug_list = []
    for i in bugs:
        bug_list.append(dict(i))
    return response.json(response_util.success(product=bug_list))