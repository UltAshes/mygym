from app import db


class users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.Enum("user", "admin"), default="user", nullable=True)
    username = db.Column(db.VARCHAR(200), nullable=False)
    password = db.Column(db.VARCHAR(200), nullable=False)
    photo = db.Column(db.VARCHAR(200), nullable=True)
    email = db.Column(db.VARCHAR(200), nullable=True)
    real_name = db.Column(db.VARCHAR(200), nullable=True)
    money = db.Column(db.Float, default=0, nullable=False)
    credit = db.Column(db.Enum("正常", "黑名单"), default="正常", nullable=False)


class order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seller_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.VARCHAR(200), nullable=False)
    description = db.Column(db.VARCHAR(200), nullable=False)
    resources = db.Column(db.VARCHAR(200), nullable=False)
    status = db.Column(db.Enum("待审核", "已通过", "已结束"), default="待审核", nullable=False)
    price = db.Column(db.Float, nullable=False)
    last_price = db.Column(db.Float, nullable=False)
    money = db.Column(db.Enum("否", "是", "已结束"), default="否", nullable=False)
    buyer_id = db.Column(db.Integer, nullable=False)


class bid(db.Model):
    __tablename__ = 'bid'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, nullable=False)
    seller_id = db.Column(db.Integer, nullable=False)
    buyer_id = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)


class message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.VARCHAR(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


