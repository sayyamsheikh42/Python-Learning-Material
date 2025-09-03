# Asynchronous Programming — Examples
import asyncio
import time

async def work(label, delay):
    await asyncio.sleep(delay)
    return f"{label} done after {delay}s"

async def main():
    start = time.time()
    results = await asyncio.gather(work("A", 1), work("B", 2))
    print(results, "elapsed:", round(time.time()-start, 2), "s")

if __name__ == "__main__":
    asyncio.run(main())
