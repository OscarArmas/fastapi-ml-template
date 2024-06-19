import aioredis

from .base_cache import BaseCache


class RedisCache(BaseCache):
    """Redis Cache Backend."""

    def __init__(self, redis_url):
        """
        Initialize RedisCache with an async Redis client.

        :param redis_url: URL of the Redis server
        """
        self.redis = aioredis.from_url(redis_url)

    async def get(self, key):
        """
        Return pair (value, found) for key asynchronously.

        :param key: the key
        """
        r = await self.redis.get(key)
        return r

    async def set(self, key, value, timeout=None):
        """
        Asynchronously set cached value key -> value with an optional timeout.

        :param key: the key
        :param value: the value
        :param timeout: timeout in seconds or None
        """
        if timeout is None:
            result = await self.redis.set(name=key, value=value)
        else:
            result = await self.redis.setex(name=key, time=timeout, value=value)
        return result

    async def has(self, key):
        """
        Asynchronously ask if cache has key.

        :param key: the key
        """
        return await self.redis.exists(key)

    async def close(self):
        """
        Close the Redis connection.
        """
        await self.redis.close()
