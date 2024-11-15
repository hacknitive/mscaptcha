from traceback import (
    format_exc,
    print_exc,
)
from logging import Logger
from typing import Optional, Any, List

from redis.asyncio import (
    Redis,
    ConnectionPool,
)
from redis.exceptions import RedisError


class AsyncRedisClient:
    """
    A singleton class to manage asynchronous Redis connections with a connection pool.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Implement the singleton pattern. If an instance already exists, return it.
        Otherwise, create a new one.
        """
        if cls._instance is None:
            cls._instance = super(AsyncRedisClient, cls).__new__(cls)
        return cls._instance

    def __init__(
        self,
        host: str = "localhost",
        port: int = 6379,
        db: int = 0,
        password: Optional[str] = None,
        max_connections: int = 10,
        decode_responses: bool = True,
        logger: Logger = None,
    ):
        """
        Initialize the Redis connection pool.

        Args:
            host (str): Redis server address.
            port (int): Redis server port.
            db (int): Redis database number.
            password (Optional[str]): Password for Redis authentication.
            max_connections (int): Maximum number of connections in the pool.
            decode_responses (bool): Whether to decode responses to strings.
        """
        self.pool = ConnectionPool(
            host=host,
            port=port,
            db=db,
            password=password,
            max_connections=max_connections,
            decode_responses=decode_responses,
        )
        self.redis_client = Redis(connection_pool=self.pool)
        self._connected = False

        self.info_logger = logger.info if logger else lambda x: print(str(x))
        self.exception_logger = logger.warning if logger else lambda x: print_exc()

    async def connect(self) -> bool:
        """
        Establish a connection to the Redis server by sending a PING command.

        Returns:
            bool: True if the connection is successful, False otherwise.
        """
        try:
            response = await self.redis_client.ping()
            self._connected = response is True
            return self._connected
        except RedisError:
            self.exception_logger(format_exc())
            self._connected = False
            return False

    async def close(self) -> None:
        """
        Gracefully close the Redis client and disconnect the connection pool.
        """
        try:
            await self.redis_client.aclose()
            await self.pool.disconnect()
            self._connected = False
            self.info_logger("[Redis] Connection closed.")
        except RedisError as e:
            self.exception_logger(format_exc())

    async def set(
        self,
        key: str,
        value: Any,
        ex: Optional[int] = None,
        px: Optional[int] = None,
        nx: bool = False,
        xx: bool = False,
    ) -> bool:
        """
        Set a key-value pair in Redis.

        Args:
            key (str): The key to set.
            value (Any): The value to associate with the key.
            ex (Optional[int]): Set the specified expire time, in seconds.
            px (Optional[int]): Set the specified expire time, in milliseconds.
            nx (bool): Only set the key if it does not already exist.
            xx (bool): Only set the key if it already exists.

        Returns:
            bool: True if the key was set, False otherwise.
        """
        try:
            result = await self.redis_client.set(key, value, ex=ex, px=px, nx=nx, xx=xx)
            return result is True
        except RedisError as e:
            self.exception_logger(format_exc())
            return False

    async def get(self, key: str) -> Optional[Any]:
        """
        Get the value of a key from Redis.

        Args:
            key (str): The key to retrieve.

        Returns:
            Optional[Any]: The value associated with the key, or None if not found.
        """
        try:
            value = await self.redis_client.get(key)
            return value
        except RedisError as e:
            self.exception_logger(format_exc())
            return None

    async def delete(self, key: str) -> int:
        """
        Delete a key from Redis.

        Args:
            key (str): The key to delete.

        Returns:
            int: Number of keys that were removed.
        """
        try:
            result = await self.redis_client.delete(key)
            return result
        except RedisError as e:
            self.exception_logger(format_exc())
            return 0

    async def exists(self, key: str) -> bool:
        """
        Check if a key exists in Redis.

        Args:
            key (str): The key to check.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        try:
            result = await self.redis_client.exists(key)
            return result == 1
        except RedisError as e:
            self.exception_logger(format_exc())
            return False

    async def flush_db(self) -> bool:
        """
        Remove all keys from the current database.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        try:
            await self.redis_client.flushdb()
            return True
        except RedisError as e:
            self.exception_logger(format_exc())
            return False

    async def keys(self, pattern: str = "*") -> List[str]:
        """
        Retrieve all keys matching a given pattern.

        Args:
            pattern (str): The pattern to match keys. Defaults to "*".

        Returns:
            List[str]: A list of matching keys.
        """
        try:
            keys = await self.redis_client.keys(pattern)
            return keys
        except RedisError as e:
            self.exception_logger(format_exc())
            return []

    async def pipeline(self, commands: List[Any]) -> List[Any]:
        """
        Execute a pipeline of Redis commands.

        Args:
            commands (List[Any]): A list of Redis commands to execute in a pipeline.

        Returns:
            List[Any]: A list of results from the executed commands.
        """
        try:
            pipe = self.redis_client.pipeline()
            for command in commands:
                method_name = command.pop(0).lower()
                method = getattr(pipe, method_name, None)
                if method:
                    method(*command)
                else:
                    raise ValueError(f"Unsupported Redis command: {method_name}")
            results = await pipe.execute()
            return results
        except RedisError as e:
            self.exception_logger(format_exc())
            return []
        except Exception as ex:
            self.exception_logger(format_exc())
            return []


# Example Usage
if __name__ == "__main__":
    import asyncio

    async def main():
        # Initialize the Redis client
        redis_client = AsyncRedisClient(
            host="localhost",
            port=6379,
            db=0,
            password="XQ75GU9x4jkc9QmL63ttqPr4ENSmY95PvjYLRXq7FSmRpMHQYT",
            max_connections=20,
            decode_responses=True,
        )

        # Connect to Redis
        connected = await redis_client.connect()
        if not connected:
            print("Failed to connect to Redis.")
            return

        # Set a key
        success = await redis_client.set("mykey", "myvalue", ex=3600)
        print(f"Set key 'mykey': {success}")

        # Get the key
        value = await redis_client.get("mykey")
        print(f"Value of 'mykey': {value}")

        # Check if key exists
        exists = await redis_client.exists("mykey")
        print(f"Does 'mykey' exist? {exists}")

        # Delete the key
        deleted = await redis_client.delete("mykey")
        print(f"Deleted 'mykey': {deleted}")

        # Flush the database
        flushed = await redis_client.flush_db()
        print(f"Flushed DB: {flushed}")

        # Close the connection
        await redis_client.close()

    # Run the example
    asyncio.run(main())
