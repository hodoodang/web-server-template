# -*- coding: utf-8 -*-
import asyncio

from fastapi import APIRouter, HTTPException

from app.core import operating, asyncio_operating, time_operating

router = APIRouter()


@router.get("/sync/", status_code=200)
def sync_api_call(duration: int = 10):
    """
    Test Concurrent Requests
    Args:
        duration: sleep 에 넘길 값

    Returns:
        id: duration
    """
    print(f"sync duration: {duration}")
    return {"id": operating(duration)}


@router.get("/async", status_code=200)
async def async_api_call(duration: int):
    """
    Test Concurrent Requests
    Args:
        duration: sleep 에 넘길 값

    Returns:
        id: duration
    """
    try:
        result = await asyncio_operating(duration)
        print(f"id: {duration}, {result}")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@router.get("/async-time", status_code=200)
async def async_api_time_call(duration: int):
    """
    Test Concurrent Requests
    Args:
        duration: sleep 에 넘길 값

    Returns:
        id: duration
    """
    try:
        result = await time_operating(duration)
        print(f"id: {duration}, {result}")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
