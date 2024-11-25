import asyncio
import aiohttp
from queue import Queue
from typing import Any, Dict, List, Optional


class HTTPRequests:
    @staticmethod
    def is_ok(response: aiohttp.ClientResponse) -> bool:
        return True if response.status == 200 else False

    @classmethod
    async def get(
            cls,
            url: str,
            headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, str]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=url,
                headers=headers
            ) as response:
                if cls.is_ok(response):
                    return await response.json()

    @classmethod
    async def post(
            cls,
            url: str,
            json: Dict[str, Any],
            headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, str]:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=url,
                json=json,
                headers=headers
            ) as response:
                if cls.is_ok(response):
                    return await response.json()

    @classmethod
    async def post_multi(
            cls,
            urls: List[str],
            jsons: List[Dict[str, Any]]
    ) -> Queue[Any]:
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url, json in zip(urls, jsons):
                task = session.post(url=url, json=json)
                tasks.append(task)
            responses = await asyncio.gather(*tasks)
            responses_queue = Queue()
            for response in responses:
                if cls.is_ok(response):
                    responses_queue.put(await response.json())
                else:
                    responses_queue.put(None)
            return responses_queue
