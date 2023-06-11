from datetime import timedelta, datetime
import jwt
from flask import jsonify, request

SECRET_KEY = "asjcklqencoiwrev45y6"
ALGORITHM = "HS256"


def create_token(username, access, uid):
    access_token_expires = timedelta(seconds=300)
    expire = datetime.utcnow() + access_token_expires
    payload = {
        "sub": username,
        "uid": uid,
        "access": access,
        "exp": expire
    }
    access_token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
    return access_token


def check_token(func):
    def wrapper():
        token = request.headers.get("Authorization")
        try:
            payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
            access = payload.get("access")
            username = payload.get("sub")
            uid = payload.get("uid")
            return func(dict(username=username, uid=uid, access=access))
        except jwt.DecodeError:
            return jsonify(code=401, message="token无权限")
        except jwt.ExpiredSignatureError:
            return jsonify(code=401, message="token已过期")
        except jwt.PyJWTError:
            return jsonify(code=401, message="无法检验token")

    wrapper.__name__ = func.__name__
    return wrapper
