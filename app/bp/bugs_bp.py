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