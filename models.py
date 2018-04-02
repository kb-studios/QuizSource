from config import app, db
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask import login

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)
    dateTime = db.Column(db.DateTime)
    tags = db.Column(db.String(200))

    def __repr__(self):
        return '<Topic %r>' % self.name

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column('user_id', db.Integer, db.ForeignKey("topic.id"), nullable=False)
    name = db.Column(db.Text)
    option1 = db.Column(db.String(80), nullable=False)
    option2 = db.Column(db.String(80), nullable=False)
    option3 = db.Column(db.String(80), nullable=False)
    option4 = db.Column(db.String(80), nullable=False)
    correct_answer = db.Column(db.SmallInteger, nullable=False)
    status = db.Column(db.SmallInteger, default=-1)

    def __repr__(self):
        return '<Question %r>' % self.question

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(320), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def set_password(self, passwd):
        self.password = passwd

    def check_password(self, passwd):
        return self.password == passwd

    def __repr__(self):
        return '<User %r>' % self.user