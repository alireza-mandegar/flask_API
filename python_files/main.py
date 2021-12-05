from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Model(db.Model):
    # id	integer : شناسه شاخص
    id = db.Column(db.Integer, primary_key=True)
    # title	string : عنوان شاخص
    title = db.Column(db.String, nullable=False)
    # slug	string : کلید شاخص
    slug = db.Column(db.String, nullable=False)
    # p	integer : قیمت شاخص به ریال
    p = db.Column(db.Integer, nullable=False)
    # d	integer : میزان تغییر
    d = db.Column(db.Integer, nullable=False)
    # dp	integer : درصد تغییر
    dp = db.Column(db.Integer, nullable=False)
    # dt	string : نوع تغییر
    dt = db.Column(db.String, nullable=False)
    # o	integer : نرخ بازگشایی شاخص
    o = db.Column(db.Integer, nullable=False)
    # h	integer : بالاترین نرخ امروز
    h = db.Column(db.Integer, nullable=False)
    # l	integer : پایین ترین نرخ امروز
    l = db.Column(db.Integer, nullable=False)
    # t	string : زمان آخرین نرخ به فرمت غیر ماشینی
    t = db.Column(db.String, nullable=False)
    # updated_at	string($date-time) : زمان آخرین نرخ به فرمت دیتابیسی
    update_at = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"model(id:{self.id}, title:{self.title}, slug:{self.slug}, p:{self.p}, " \
               f"d:{self.d}, dp:{self.dp}, dt:{self.dt}, o:{self.o}, h:{self.h}, " \
               f"l:{self.l}, t:{self.t}, updated_at:{self.update_at})"


# db.create_all() db has been created don't run this line

model_put_args = reqparse.RequestParser()
model_put_args.add_argument("id", type=int, help="id of model", required=True)
model_put_args.add_argument("title", type=str, help="title of model", required=True)
model_put_args.add_argument("slug", type=str, help="slug of model", required=True)
model_put_args.add_argument("p", type=int, help="p of model", required=True)
model_put_args.add_argument("d", type=int, help="d of model", required=True)
model_put_args.add_argument("dp", type=int, help="dp of model", required=True)
model_put_args.add_argument("dt", type=str, help="dt of model", required=True)
model_put_args.add_argument("o", type=int, help="o of model", required=True)
model_put_args.add_argument("h", type=int, help="h of model", required=True)
model_put_args.add_argument("l", type=int, help="l of model", required=True)
model_put_args.add_argument("t", type=str, help="t of model", required=True)
model_put_args.add_argument("update_at", type=str, help="update_at of model", required=True)

resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'slug': fields.String,
    'p': fields.Integer,
    'd': fields.Integer,
    'dp': fields.Integer,
    'dt': fields.String,
    'o': fields.Integer,
    'h': fields.Integer,
    'l': fields.Integer,
    't': fields.String,
    'update_at': fields.String
}
