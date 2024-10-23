""" """

from fastapi import FastAPI



def setup_routers(app: FastAPI) -> None:
    """ """
    pass


def create_application() -> FastAPI:
    """ """

    application = FastAPI()

    setup_routers(application)

    return application