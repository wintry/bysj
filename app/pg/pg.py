import asyncpg
from config import settings


'''postgres的默认配置'''
# reate_pool(dsn=None, *, min_size=10, max_size=128, max_queries=50000, max_inactive_connection_lifetime=300.0,
#  setup=None, init=None, loop=None, connection_class=<class 'asyncpg.connection.Connection'>, **connect_kwargs)

#创建数据库连接池
async def setup_connection():
    global db_pool
    db_pool =await asyncpg.create_pool(max_size=20,**settings.DB_CONFIG)
    return db_pool

#关闭数据库连接池
async def close_connection():
    await db_pool.close()
