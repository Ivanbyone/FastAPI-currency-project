""" """

from src.factory.config import settings
from src.application.common.currency_list_dto import CurrencyListDTO
from src.infrastructure.external_api.base_client import BaseClient
from src.infrastructure.external_api.aiohttp_client import AiohttpClient
from src.infrastructure.redis.base_redis import RedisBase, RedisClient


class GetCurrencyListUseCase:
    """ """

    def __init__(self):
        self.client: BaseClient = AiohttpClient(
            headers={
                "x-cg-pro-api-key": settings.API_KEY
            },
            url='https://api.coingecko.com/api/v3/coins/list')
        self.redis_client: RedisBase = RedisClient()

    async def __call__(self) -> CurrencyListDTO:
        """ """
        data = await self.redis_client.get_cached(key="currency")
        if data is not None:
            print("Using cached by Redis")
            return data

        response = await self.client.get_method()
        print("Using API call")
        keys = ['name', 'symbol']
        filtered_response = [
            {k: item[k].upper() for k in keys if k in item}
            for item in response
        ]
        await self.redis_client.cached(key="currency", value=filtered_response, ttl=200)
        return filtered_response
    