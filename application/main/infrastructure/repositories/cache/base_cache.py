from abc import ABC, abstractmethod

class BaseCache(ABC):
    """
    Abstract base class for cache backends.
    """

    @abstractmethod
    async def get(self, key):
        """
        Asynchronously get a value from the cache.
        
        :param key: the key
        :return: a tuple (value, found)
        """
        pass

    @abstractmethod
    async def set(self, key, value, timeout=None):
        """
        Asynchronously set a value in the cache with an optional timeout.
        
        :param key: the key
        :param value: the value to store
        :param timeout: optional timeout in seconds
        """
        pass

    @abstractmethod
    async def has(self, key):
        """
        Asynchronously check if a key exists in the cache.
        
        :param key: the key
        :return: True if the key exists, False otherwise
        """
        pass

    @abstractmethod
    async def close(self):
        """
        Asynchronously close any connections or clean up resources.
        """
        pass
