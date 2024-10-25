""" """
import asyncio
import aiohttp
from fastapi import APIRouter

from src.application.use_cases.get_currency_list import GetCurrencyListUseCase
from src.application.common.currency_list_dto import CurrencyListDTO


router: APIRouter = APIRouter()


@router.get(path='/list/', response_model=list[CurrencyListDTO])
async def get_currency_list():
    """ """
    return await GetCurrencyListUseCase().__call__()
