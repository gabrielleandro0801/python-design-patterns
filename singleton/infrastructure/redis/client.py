import redis


class Cache:
    _instance = None

    def __init__(self, url: str) -> None:
        self.connection = redis.Redis.from_url(url)

    @classmethod
    def get_instance(cls, connection):
        if cls._instance is None:
            cls._instance = cls(connection)
        return cls._instance

    def get(self, key: str) -> str or None:
        try:
            if key is None:
                return None
            cached_value = self.connection.get(key)
            return cached_value.decode('utf-8') if cached_value is not None else None
        except Exception:
            return None

    def set(self, key: str, value: str, time: int) -> None:
        try:
            self.connection.set(key, value, ex=time)
        except Exception:
            pass
