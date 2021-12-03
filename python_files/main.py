from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, nullable=False)
    p = db.Column(db.Integer, nullable=False)
    d = db.Column(db.Integer, nullable=False)
    dp = db.Column(db.Integer, nullable=False)
    dt = db.Column(db.String, nullable=False)
    o = db.Column(db.Integer, nullable=False)
    h = db.Column(db.Integer, nullable=False)
    l = db.Column(db.Integer, nullable=False)
    t = db.Column(db.String, nullable=False)
    update_at = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"model(id:{self.id}, title:{self.title}, slug:{self.slug}, p:{self.p}, d:{self.d}, dp:{self.dp}, dt:{self.dt}, o:{self.o}, h:{self.h}, l:{self.l}, t:{self.t}, updated_at:{self.update_at})"

# db.create_all() db has been created don't run this line

