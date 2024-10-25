""" """

from abc import abstractmethod
from typing import Protocol


class BaseUseCase(Protocol):
    """ """

    @abstractmethod
    async def __call__(self, *args, **kwargs):
        raise NotImplementedError
