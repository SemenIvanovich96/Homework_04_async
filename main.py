import asyncio
from models import engine, Base, AsyncSessionLocal, User, Post
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from sqlalchemy.ext.asyncio import AsyncSession

async def init_db():
    """Создает таблицы."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def add_users(session: AsyncSession, users_data: list[dict]):
    """Добавляет пользователей."""
    for data in users_data:
        user = User(name=data['name'], username=data['username'], email=data['email'])
        session.add(user)
    await session.commit()


async def add_posts(session: AsyncSession, posts_data: list[dict]):
    """Добавляет посты."""
    for data in posts_data:
        post = Post(user_id=data['userId'], title=data['title'], body=data['body'])
        session.add(post)
    await session.commit()


async def async_main():
    """Основной асинхронный цикл."""
    await init_db()

    async with AsyncSessionLocal() as session:

        users_data, posts_data = await asyncio.gather(
            fetch_users_data(),
            fetch_posts_data()
        )


        await add_users(session, users_data)
        await add_posts(session, posts_data)

    await engine.dispose()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()