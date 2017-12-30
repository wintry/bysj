import json

from sanic import Blueprint,response

from app.exceptions import  app_exception


from utils import MD5_util,response_util,data_util
bugs_bp=Blueprint('bugs_bp',url_prefix='/bugs')


@bugs_bp.post('/add_bug')
async def add_bug(request):
    user = await  data_util.token(request, 1)
    if user == False:
        return response.json({"status": "002", "message": "no permission"})

    data = request.json


    async with bugs_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''insert into  "bugs" (title, detail, img, product_id, line_id, create_time,user_id) values ($1,$2,$3,$4,$5,$6,$7) ''')
        await stmt.fetchrow(data['title'],data['detail'],data['img'],data['product_id'],data['line_id'],data['time'],user['id'])
    return response.json({"status": "succeed"})

@bugs_bp.post('/edit_bug')
async def edit_bug(request):
    user = await  data_util.token(request, 1)
    if user == False:
        return response.json({"status": "002", "message": "no permission"})
    data = request.json
    async with bugs_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''select * from "bugs" WHERE id = $1''')
        bug = dict(await stmt.fetchrow(data['id']))
    if bug['user_id']!=user['id'] and user['lv']<2:
        return response.json({"status": "002", "message": "no permission"})
    async with bugs_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''update  "bugs" set  title=$1, detail=$2, img=$3, product_id=$4, line_id=$5, create_time=$6 where id = $7 ''')
        await stmt.fetchrow(data['title'],data['detail'],data['img'],data['product_id'],data['line_id'],data['time'],data['id'])
    return response.json({"status": "succeed"})

@bugs_bp.post('/se_bug')
async def se_bugs(request):
    user = await  data_util.token(request, 1)
    if user == False:
        return response.json({"status": "002", "message": "no permission"})

    data = request.json
    async with bugs_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''select * from "bugs" WHERE title ~ $1''')
        bugs = await stmt.fetch(data['key'])
    bug_list = []
    for i in bugs:
        bug_list.append(dict(i))
    return response.json(response_util.success(product=bug_list))

@bugs_bp.get('/get_bugs')
async def get_bugs(request):
    user = await  data_util.token(request, 1)
    if user == False:
        return response.json({"status": "002", "message": "no permission"})

    async with bugs_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''select * from "bugs" ORDER BY id DESC ''')
        bugs = await stmt.fetch()
    bug_list = []
    for i in bugs:
        bug_list.append(dict(i))
    return response.json(response_util.success(product=bug_list))