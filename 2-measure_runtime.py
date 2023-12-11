#!/usr/bin/env python3
""" Async basics in Python task 2 """

import asyncio
import random

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime """
    start = asyncio.get_event_loop().time()
    await wait_n(n, max_delay)
    end = asyncio.get_event_loop().time()
    return (end - start) / n
