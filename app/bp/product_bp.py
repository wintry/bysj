import json

from sanic import Blueprint,response

from app.exceptions import  app_exception


from utils import MD5_util,response_util,data_util
product_bp=Blueprint('product_bp',url_prefix='/product')


@product_bp.post('/add_product')
async def add_product(request):
    user = await  data_util.token(request, 3)
    if user == False:
        return response.json({"status": "002", "message": "no permission"})

    data = request.json


    async with product_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''insert into  "product" (name,fid) values ($1,$2) ''')
        await stmt.fetchrow(data['name'],0)
    return response.json({"status": "succeed"})



@product_bp.post('/edit_product')
async def edit_product(request):
    user = await  data_util.token(request, 3)
    if user == False:
        return response.json({"status": "002", "message": "no permission"})
    data = request.json
    try:
        data['product_id']
        data['name']
    except KeyError as e:
        raise app_exception.params_error(str(e)+'is empty or wrong')
    
    async with product_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''update  "product" set  name = $1 where id = $2 ''')
        await stmt.fetchrow(data['name'],data['product_id'])
    return response.json({"status": "succeed"})

@product_bp.post('/del_product')
async def del_product(request):
    user = await  data_util.token(request, 3)
    if user == False:
        return response.json({"status": "002", "message": "no permission"})
    data = request.json

    async with product_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''select * from "product" WHERE id = $1''')
        product = dict(await stmt.fetchrow(data['product_id']))

    async with product_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''delete from  "product" where id = $1 ''')
        await stmt.fetchrow(data['product_id'])
    if product['fid'] == 0:
        async with product_bp.pool.acquire() as conn:
            stmt = await conn.prepare('''delete from  "product" where fid = $1 ''')
            await stmt.fetchrow(data['product_id'])

    return response.json({"status": "succeed"})



@product_bp.post('/add_line')
async def add_line(request):
    user = await  data_util.token(request, 3)
    if user == False:
        return response.json({"status": "002", "message": "no permission"})
    data = request.json
    try:
        data['product_id']
        data['name']
    except KeyError as e:
        raise app_exception.params_error(str(e)+'is empty or wrong')
    
    async with product_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''insert into  "product" (name,fid) values ($1,$2) ''')
        await stmt.fetchrow(data['name'],data['product_id'])
    return response.json({"status": "succeed"})


@product_bp.post('/get_line')
async def get_line_by_product(request):
    user = await  data_util.token(request, 1)
    if user == False:
        return response.json({"status": "002", "message": "no permission"})
    data = request.json
    async with product_bp.pool.acquire() as conn:
        stmt = await conn.prepare('''select * from "product" WHERE fid = $1''')
        product = await stmt.fetch(data['product_id'])
    product_list=[]
    for i in product:
        product_list.append(dict(i))
    return response.json(response_util.success(product=product_list))


# @product_bp.get('/get_all_product')
# @data_util.token_check_three
# async def add_line(request):