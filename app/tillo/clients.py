from jpy_tillo_sdk.http_client_factory import create_client_async, create_client

from ..config import TILLO_API_KEY, TILLO_SECRET, TILLO_HTTP_CLIENT_OPTIONS

tillo_client_async = create_client_async(
    TILLO_API_KEY,
    TILLO_SECRET,
    TILLO_HTTP_CLIENT_OPTIONS,
)

tillo_client = create_client(
    TILLO_API_KEY,
    TILLO_SECRET,
    TILLO_HTTP_CLIENT_OPTIONS,
)