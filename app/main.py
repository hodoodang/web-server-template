import asyncio
from asyncio.windows_events import ProactorEventLoop

import uvicorn
from uvicorn import Config, Server
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.errors import ServerErrorMiddleware

from app.utils import init_logging
from app.api import api_router


def create_app():
    # TODO: get Config

    application = FastAPI()

    init_logging()
    # TODO: init DB

    # TODO: middleware initialize and add
    # Token Check
    # application.add_middleware(BaseHTTPMiddleware)
    # Allow CORS
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    # API URI Check
    # application.add_middleware(
    #     TrustedHostMiddleware,
    #     allowed_hosts="^(/docs|/redoc|/api|/analyze|/tests)"
    # )
    application.add_middleware(ServerErrorMiddleware)

    application.include_router(api_router)
    return application


class ProactorServer(Server):
    def run(self, sockets=None):
        loop = ProactorEventLoop()
        asyncio.set_event_loop(loop)
        asyncio.run(self.serve(sockets=sockets))


app = create_app()


if __name__ == "__main__":

    uvicorn.run(app="main:app",
                host="0.0.0.0",
                port=80,
                reload=True,
                workers=4)

    # config = Config(app=app, host="0.0.0.0", port=80, reload=True)
    # server = ProactorServer(config=config)
    # server.run()
