#!/usr/bin/env python3
""" Take the code from wait_n and alter it into a new function task_wait_n.
    The code is nearly identical to wait_n except task_wait_random is being
    called. """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Execute multiple task_wait_random coroutines concurrently and collect results """
    delays: List[float] = [
    ]       # List to hold the task_wait_random coroutines
    all_delays: List[float] = []   # List to store the collected delay results

    """ Spawn n task_wait_random coroutines with the specified max_delay"""
    for i in range(n):
        delays.append(task_wait_random(max_delay))

    """ Wait for tasks to complete using asyncio.as_completed"""
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)

    return all_delays
