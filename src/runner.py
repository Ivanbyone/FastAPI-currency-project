""" App's entrypoint """

import uvicorn


if __name__ == '__main__':
    uvicorn.run('src.factory.app:create_application',
                factory=True,
                reload=True)
