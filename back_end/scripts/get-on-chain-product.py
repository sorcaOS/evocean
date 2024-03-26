import base64

import asyncio
import requests
from solana.rpc.api import Client
from solana.rpc.async_api import AsyncClient


async def main():
    async with AsyncClient("http://localhost:8899") as client:
        res = await client.is_connected()
    print(res)  # True

    # Alternatively, close the client explicitly instead of using a context manager:
    client = AsyncClient("http://localhost:8899")
    res = await client.is_connected()

    client

    await client.close()

asyncio.run(main())