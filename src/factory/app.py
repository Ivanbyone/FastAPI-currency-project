""" """

from fastapi import FastAPI

from src.presentation.currency_router import router as currency_router
from src.infrastructure.redis.redis_pool import create_pool


def setup_routers(app: FastAPI) -> None:
    """ """
    app.include_router(
        router=currency_router,
        prefix='/currency',
        tags=["Currency"]
    )


def create_application() -> FastAPI:
    """ """

    application = FastAPI()

    setup_routers(application)

    @application.on_event('startup')
    async def on_startup():
        pool = create_pool()
        await pool.get_connection('_')

    @application.on_event("shutdown")
    async def shutdown_event():
        await create_pool().disconnect()

    return application


#  docker run -p 6379:6379 --name redis -d redis
