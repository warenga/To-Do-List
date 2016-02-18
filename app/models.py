from . import db
from flask import request
from flask import current_app
import json


class Lis(db.Model):
	__tablename__ = 'lists'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), unique=True)
	tasks = db.relationship('Tasks', backref='lis', lazy='dynamic')

	def __repr__(self):
		return '<Title %r>' % self.title

class Tasks(db.Model):
	__tablename__ = 'tasks'
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.Text(64), unique=True, index=True)
	done = db.Column(db.Boolean, default=False)
	lis_id = db.Column(db.Integer, db.ForeignKey('lists.id'))

	def __repr__(self):
		status = 'done' if self.done else 'open'
		return '<{0> tasks: {1} by {2}>'.format(
			status, self.done )

	def to_json(self):
		json_tasks = {
			'body': self.body,
			'done': self.done,
			'status': 'done' if self.done else 'open'
		}
		return json_tasks

	@staticmethod
	def from_json(json_tasks):
		Tasks(Json.loads(json_tasks)).save()