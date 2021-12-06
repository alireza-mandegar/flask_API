from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Model(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    # id	integer : شناسه شاخص
    id = db.Column(db.Integer, primary_key=False)
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
    updated_at = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"model(id:{self.id}, title:{self.title}, slug:{self.slug}, p:{self.p}, " \
               f"d:{self.d}, dp:{self.dp}, dt:{self.dt}, o:{self.o}, h:{self.h}, " \
               f"l:{self.l}, t:{self.t}, updated_at:{self.updated_at})"


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
model_put_args.add_argument("updated_at", type=str, help="updated_at of model", required=True)

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
    'updated_at': fields.String
}


class Url(Resource):
    @marshal_with(resource_fields)
    def get(self, data_id):
        result = Model.query.filter_by(id=data_id).all()
        if not result:
            abort(404, message="Could not find data with that id")
        return result

    @marshal_with(resource_fields)
    def put(self, data_id):
        args = model_put_args.parse_args()
        result = Model.query.filter_by(id=data_id).first()
        if result:
            abort(409, message="data id taken...")

        data = Model(id=data_id, title=args['title'], slug=args['slug'],
                     p=args['p'], d=args['d'], dp=args['dp'], dt=args['dt'],
                     o=args['o'], h=args['h'], l=args['l'], t=args['t'],
                     updated_at=args['updated_at'])
        db.session.add(data)
        db.session.commit()
        return data, 201


api.add_resource(Url, "/get_or_put_data/<int:data_id>")

if __name__ == "__main__":
    app.run(debug=True)
