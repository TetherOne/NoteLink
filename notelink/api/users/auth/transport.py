from fastapi_users.authentication import BearerTransport

from notelink.core.settings.config import settings

bearer_transport = BearerTransport(
    tokenUrl=settings.api.full_prefix_for_bearer_transport,
)
