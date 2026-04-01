import aiohttp
from typing import List, Dict

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

async def fetch_json(session: aiohttp.ClientSession, url: str) -> List[Dict]:
    """Базовая функция для GET-запроса JSON."""
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json()

async def fetch_users_data() -> List[Dict]:
    """Загружает список пользователей."""
    async with aiohttp.ClientSession() as session:
        return await fetch_json(session, USERS_DATA_URL)

async def fetch_posts_data() -> List[Dict]:
    """Загружает список постов."""
    async with aiohttp.ClientSession() as session:
        return await fetch_json(session, POSTS_DATA_URL)