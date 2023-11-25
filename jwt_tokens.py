import datetime

import jwt

import settings

payload = {
    "my_name": "Evgeny",
    "age": 21,
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60),
}


def encode_jwt(playloadd: dict) -> str:
    return jwt.encode(
        payload=payload,
        key=settings.JWT_SECRET,
        algorithm="HS256",
    )


print(encode_jwt)
data = encode_jwt
decoded = jwt.decode(
    encode_jwt,
    settings.JWT_SECRET,
    algorithms=["HS256"],
    # options={
    #     'verify_signature': False,
    # }
)
print(decoded)
