import time
import uuid
import loguru
import contextvars

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


logger = loguru.logger
request_id_contextvar = contextvars.ContextVar("request_id", default=None)


async def request_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    with logger.contextualize(request_id=request_id):
        logger.info(f"Request {request_id} started")

        try:
            return await call_next(request)

        except Exception as e:
            logger.error(f"Request failed: {e}")
            return JSONResponse(content={"success": False}, status_code=500)

        finally:
            logger.info(f"Request {request_id} ended")
