import base64
import functools
import re
import uuid

from notelink.core.helpers.cache_helper import AsyncRedisCache

cache = AsyncRedisCache()


def cache_decorator(cache_key: str):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            cached_result = await cache.get(cache_key)
            if cached_result:
                return cached_result
            result = await func(*args, **kwargs)
            await cache.set(cache_key, result)
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
