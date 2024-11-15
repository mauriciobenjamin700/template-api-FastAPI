from fastapi import HTTPException


def NotFound(detail: str) -> HTTPException:
    return HTTPException(status_code=404, detail=detail)


def BadRequest(detail: str) -> HTTPException:
    return HTTPException(status_code=400, detail=detail)


def Unauthorized(detail: str) -> HTTPException:
    return HTTPException(status_code=401, detail=detail)


def Forbidden(detail: str) -> HTTPException:
    return HTTPException(status_code=403, detail=detail)


def Conflict(detail: str) -> HTTPException:
    return HTTPException(status_code=409, detail=detail)


def TooManyRequests(detail: str) -> HTTPException:
    return HTTPException(status_code=429, detail=detail)


def ServerError(detail: str) -> HTTPException:
    return HTTPException(status_code=500, detail=detail)


def ServiceUnavailable(detail: str) -> HTTPException:
    return HTTPException(status_code=503, detail=detail)


def GatewayTimeout(detail: str) -> HTTPException:
    return HTTPException(status_code=504, detail=detail)


def NotImplemented(detail: str) -> HTTPException:
    return HTTPException(status_code=501, detail=detail)


def BadGateway(detail: str) -> HTTPException:
    return HTTPException(status_code=502, detail=detail)

