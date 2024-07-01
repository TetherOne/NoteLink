from fastapi_users.authentication import AuthenticationBackend

from notelink.api.authentication.strategy import get_database_strategy
from notelink.auth.transport import bearer_transport


authentication_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
