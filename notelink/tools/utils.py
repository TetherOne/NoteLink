import base64
import re
import uuid
from functools import wraps
from typing import Callable

from notelink.core.helpers.cache_helper import AsyncRedisCache

cache = AsyncRedisCache()


def cache_decorator(cache_key: str):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            skip = kwargs.get("skip", 0)
            limit = kwargs.get("limit", 10)
            key = f"{cache_key}_skip{skip}_limit{limit}"
            cache = AsyncRedisCache()
            cached_data = await cache.get(key)
            if cached_data:
                return cached_data

            result = await func(*args, **kwargs)
            await cache.set(key, result)
            return result

        return wrapper

    return decorator


def generate_public_id():
    raw_id = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode("utf-8")
    public_id = re.sub(r"[^a-z0-9]", "", raw_id.lower())[:6]
    return public_id


def generate_private_id():
    raw_id = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode("utf-8")
    private_id = re.sub(r"[^a-z0-9]", "", raw_id.lower())[:48]
    return private_id


def create_public_and_private(note_create):
    if note_create.is_public:
        private_id = None
        public_id = generate_public_id()
    else:
        public_id = None
        private_id = generate_private_id()
    return public_id, private_id
