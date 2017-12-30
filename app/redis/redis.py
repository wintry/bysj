import redis


pool = redis.ConnectionPool(port=6379)


def get_redis_client():
    return redis.StrictRedis(connection_pool=pool)
