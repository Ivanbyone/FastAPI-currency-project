""" """

import json

from abc import abstractmethod
from typing import Protocol, Any

import aioredis


class RedisBase(Protocol):

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    async def cached(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_cached(self, *args, **kwargs):
        raise NotImplementedError


class RedisClient:

    def __init__(self, host: str, port: int):
        self.redis = aioredis.from_url(url=f'redis://{host}:{port}')

    async def cached(self, key: str, value: Any, ttl: int):
        serialized_data = json.dumps(value, ensure_ascii=False)
        await self.redis.set(name=key, value=serialized_data, ex=ttl)

    async def get_cached(self, key: str):
        """ """
        data = await self.redis.get(key)
        if data is not None:
            deserialized_data = json.loads(data)
            return deserialized_data
        return None
