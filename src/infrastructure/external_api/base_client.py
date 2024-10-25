""" Abstract class for aiohttp client """

from typing import Protocol
from abc import abstractmethod


class BaseClient(Protocol):
    """ Base client for requests to external API """

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    async def get_method(self, *args):
        """ """
        raise NotImplementedError
