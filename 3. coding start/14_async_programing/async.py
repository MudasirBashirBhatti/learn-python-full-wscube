# Think of async / await in Python as a way to handle waiting tasks efficiently without blocking everything else—especially useful for I/O operations like network calls, file reads, APIs, etc.

import asyncio
async def task_a():
    print("Task A started")
    await asyncio.sleep(3)
    print("Task A completed")

async def task_b():
    print("Task B started")
    await asyncio.sleep(1)
    print("Task B completed")

async def task_c():
    print("Task C started")
    await asyncio.sleep(2)
    print("Task C completed")

async def main():
    t1 = asyncio.create_task(task_a())
    t2 = asyncio.create_task(task_b())
    t3 = asyncio.create_task(task_c())
    await asyncio.gather(t1, t2, t3)

asyncio.run(main())