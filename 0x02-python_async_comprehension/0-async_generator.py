#!/usr/bin/env python3
""" Async basics in Python task 0 """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ The coroutine will loop 10 times """
    res = []
    for _ in range(10):
        await asyncio.sleep(1)
        res.append(random.uniform(0, 10))
    return res
