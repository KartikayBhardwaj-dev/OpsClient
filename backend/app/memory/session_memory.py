from app.memory.redis_client import redis_client

class SessionMemory:
    @staticmethod
    async def set_session(
        session_id: str,
        data: str
    ):
        await redis_client.set(
            session_id,
            data
        )
    @staticmethod
    async def get_session(
        session_id: str
    ):
        return await redis_client.get(
            session_id
        )