# -*- coding: utf-8 -*-
import time
import asyncio


def operating(id: int):
    time.sleep(id)
    return {"duration": id}


async def time_operating(duration: int):
    time.sleep(duration)
    return {"duration": duration}


async def asyncio_operating(duration: int):
    await asyncio.sleep(duration)
    return {"duration": duration}
