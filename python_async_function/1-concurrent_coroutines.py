#!/usr/bin/env python3
'''an async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay. You will
spawn wait_random n times with the specified max_delay'''

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''an async routine called wait_n that takes in 2 int
    arguments (in this order): n and max_delay. You will
    spawn wait_random n times with the specified max_delay'''
    tasks = [wait_random(max_delay) for num in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
