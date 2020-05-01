METHOD_DELETE = "DELETE"
METHOD_GET = "GET"
METHOD_HEAD = "HEAD"
METHOD_OPTIONS = "OPTIONS"
METHOD_PATCH = "PATCH"
METHOD_POST = "POST"
METHOD_PUT = "PUT"

DEFAULT_METHODS = ",".join(
    [METHOD_GET, METHOD_HEAD, METHOD_PATCH, METHOD_POST, METHOD_DELETE]
)
