from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skill_gap_analyzer.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    skills = db.Column(db.String(500), nullable=False)  # Comma-separated skills


class JobRequirement(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    required_skills = db.Column(db.String(500), nullable=False)  # Comma-separated skills


db.create_all()

