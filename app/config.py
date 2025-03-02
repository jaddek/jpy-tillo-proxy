from dotenv import load_dotenv
import os
from httpx import Timeout, Limits

load_dotenv(override=False)

APP_NAME = os.getenv("APP_NAME", "Proxy")
TILLO_API_KEY = os.getenv("TILLO_API_KEY", "")
TILLO_SECRET = os.getenv("TILLO_SECRET", "")

TILLO_HTTP_CLIENT_OPTIONS = {
    "verify": os.getenv("TILLO_HTTP_CLIENT_OPTIONS_VERIFY", True),
    "trust_env": os.getenv("TILLO_HTTP_CLIENT_OPTIONS_TRUST_ENV", True),
    "http1": os.getenv("TILLO_HTTP_CLIENT_OPTIONS_HTTP1", False),
    "http2": os.getenv("TILLO_HTTP_CLIENT_OPTIONS_HTTP2", True),
    "timeout": Timeout(timeout=os.getenv("TILLO_HTTP_CLIENT_OPTIONS_TIMEOUT", 5.0)),
    "follow_redirects": os.getenv("TILLO_HTTP_CLIENT_OPTIONS_FOLLOW_REDIRECTS", False),
    "limits": Limits(
        max_connections=os.getenv("TILLO_HTTP_CLIENT_OPTIONS_MAX_CONNECTIONS", 100),
        max_keepalive_connections=os.getenv(
            "TILLO_HTTP_CLIENT_OPTIONS_MAX_KEEPALIVE_CONNECTIONS", 20
        ),
    ),
    "base_url": os.getenv("TILLO_HOST", ""),
    "max_redirects": os.getenv("TILLO_HTTP_CLIENT_OPTIONS_MAX_REDIRECTS", 20),
    "default_encoding": os.getenv(
        "TILLO_HTTP_CLIENT_OPTIONS_DEFAULT_ENCODING", "utf-8"
    ),
}
