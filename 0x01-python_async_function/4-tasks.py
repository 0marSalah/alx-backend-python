#!/usr/bin/env python3
""" Async basics in Python task 4 """
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns a list of delays in ascending order """
    delays: List[float] = []
    tasks = [task_wait_random(max_delay) for i in range(n)]
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return sorted(delays)
