""" """

import aiohttp

from src.infrastructure.external_api.base_client import BaseClient


class InfractructureException(Exception):
    pass


class AiohttpClient(BaseClient):

    def __init__(self, headers: dict, url: str):
        self.headers = headers
        self.url = url

    async def get_method(self):
        try:
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
                async with session.get(url=self.url, headers=self.headers, ssl=False) as response:
                    data = await response.json()
                    return data
        except Exception:
            raise InfractructureException("Aiohttp error")
