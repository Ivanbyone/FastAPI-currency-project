""" """

import aioredis

from src.factory.config import settings


def create_pool() -> aioredis.ConnectionPool:
    pool: aioredis.ConnectionPool = aioredis.ConnectionPool(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
    return pool
