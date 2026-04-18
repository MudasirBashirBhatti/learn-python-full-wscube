# Think of async / await in Python as a way to handle waiting tasks efficiently without blocking everything else—especially useful for I/O operations like network calls, file reads, APIs, etc.

# import asyncio
# async def task_a():
#     print("Task A started")
#     await asyncio.sleep(3)
#     print("Task A completed")

# async def task_b():
#     print("Task B started")
#     await asyncio.sleep(1)
#     print("Task B completed")

# async def task_c():
#     print("Task C started")
#     await asyncio.sleep(2)
#     print("Task C completed")

# async def main():
#     t1 = asyncio.create_task(task_a())
#     t2 = asyncio.create_task(task_b())
#     t3 = asyncio.create_task(task_c())
#     await asyncio.gather(t1, t2, t3)

# asyncio.run(main())

import asyncio
import random

async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)

    if random.random() < 0.3:
        raise Exception(f"{name} failed")

    print(f"{name} completed")
    return name

async def main():
    tasks = [
        asyncio.create_task(task("A", 3)),
        asyncio.create_task(task("B", 1)),
        asyncio.create_task(task("C", 2)),
    ]

    results = await asyncio.gather(*tasks, return_exceptions=True)

    print("\nResults:")
    for r in results:
        if isinstance(r, Exception):
            print("❌ Failed:", r)
        else:
            print("✅ Success:", r)

asyncio.run(main())