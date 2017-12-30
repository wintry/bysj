from sanic import Sanic,response


from app.exceptions import app_exception
from app.bp.user_bp import user_bp
from app.bp.product_bp import product_bp
from app.bp.bugs_bp import bugs_bp
from app.pg.pg import *



app = Sanic(__name__)


#register blueprint
app.blueprint(user_bp)
app.blueprint(product_bp)
app.blueprint(bugs_bp)


@app.listener('after_server_start')
async def notify_server_started(app, loop):
    db_pool = await setup_connection()
    user_bp.pool = db_pool
    product_bp.pool = db_pool
    bugs_bp.pool= db_pool
    pass


#服务器stop
@app.listener('after_server_stop')
async def notify_server_stoped(app, loop):
    pass


#异常管理
@app.exception(app_exception.appexception)
async def params_error(request,exception):
    return response.text(exception.to_dict())

if __name__ == "__main__":
    '''
    sanic 启动
    '''


    app.run(host="0.0.0.0", port='8080' )