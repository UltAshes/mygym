import hashlib
from flask import jsonify, request
from flask_cors import CORS
from app import db
from app.main import user
from app.main.util import create_token
from app.model import users

CORS(user, supports_credentials=True)


@user.route('/register/send/<phone>', methods=['get'])
def sendCode(phone):
    print(phone)
    import random
    digits = []
    for i in range(6):
        digits.append(str(random.randint(1, 8)))
    result = ''.join(digits)
    return jsonify(code=200, message="成功", data=result, ok=True)


@user.route('/register/create', methods=['POST', 'OPTIONS'])
# {
#     "username": "asdasd",
#     "password": "asdasd"
# }
def register():
    get_json = request.get_json()
    ch = users.query.filter(users.username == get_json.get('phone')).first()
    if ch is not None:
        return jsonify(code=400, message="手机号已存在")
    else:
        try:
            a = users(username=get_json.get('phone'),
                      password=hashlib.sha256(get_json.get('password').encode("utf-8")).hexdigest())
            print(a)
            db.session.add(a)
            db.session.commit()
            return jsonify(code=200, message="注册成功")
        except Exception as e:
            print("exception", e)
            return jsonify(code=401, message='填入失败')


@user.route('/login', methods=['POST', 'OPTIONS'])
# {
#     "type": "user"/"admin",
#     "username": "asdasd",
#     "password": "asdasd"
# }
def login():
    idata = {}
    get_json = request.get_json()
    access = "user"
    username = get_json.get("phone")
    password = hashlib.sha256(get_json.get('password').encode("utf-8")).hexdigest()
    ch = users.query.filter(users.type == access).filter(users.username == username).first()
    if ch is not None:
        if ch.password != password:
            return jsonify(code=400, message="密码错误")
        else:
            idata.update(username=username)
            search = users.query.filter(users.username == get_json.get('phone')).first()
            uid = search.id
            idata.update(id=uid)
            access_token = create_token(username, access, uid)
            idata.update(token=access_token)
            return jsonify(code=200, message="success", data=idata)
    else:
        return jsonify(code=400, message="用户名不存在")
