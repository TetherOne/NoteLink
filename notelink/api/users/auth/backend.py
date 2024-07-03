from fastapi_users.authentication import AuthenticationBackend

from notelink.api.users.dependencies import get_database_strategy
from notelink.api.users.auth.transport import bearer_transport


authentication_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
