from app import db,login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64),index=True,unique=True)
	hashed_password = db.Column(db.String(128))

	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self,password):
		self.hashed_password = generate_password_hash(password)

	def check_password(self,password):
		return check_password_hash(self.hashed_password,password)

	def save(self):
		if self.hashed_password is None:
			raise Exception("Password not set")
		db.session.add(self)
		db.session.commit()
	
	def delete(self):
		db.session.delete(self)
		return

class Organization(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(64),index=True)
	website = db.Column(db.String(128))
	mission = db.Column(db.String(512))
	#to be added technoloifes

	def __repr__(self):
		return '<Organization {}>'.format(self.name)

	def save(self):
		db.session.add(self)
		db.session.commit()
		return

	def delete(self):
		db.session.delete(self)
		return

	def exists(self):
		if Organization.query.filter_by(name=self.name).first() is None:
			return False
		return True

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))