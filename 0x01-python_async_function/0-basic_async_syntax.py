#!/usr/bin/env python3
""" Async basics in Python task 0 """
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous coroutine that takes in an integer argument """

    random_float = __import__('random').uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
