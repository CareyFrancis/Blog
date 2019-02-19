from . import db,login_manager
from datetime import datetime
from flask_login import UserMixin

class User(db.Model,UserMixin):
   '''
   User table model.
   Will take user's name, username, email, password, avatar, and bio.
   '''
   __tablename__ = 'users'

   id = db.Column(db.Integer, primary_key=True)
   #name = db.Column(db.String(254), nullable=False)
   username = db.Column(db.String(40), unique=True, nullable=False)
   email = db.Column(db.String(50), unique=True, nullable=False)
   password = db.Column(db.String(30), nullable=False)
   avatar = db.Column(db.String(20), default='default.jpg')
   bio = db.Column(db.String(254))
   posts = db.relationship('Posts', backref='author', lazy=True)
   #comments = db.Column('Comments', backref= 'author',lazy =True)

   def __repr__(self):
      return f"Users('{self.username}', '{self.email}')"

class Posts(db.Model):

   __tablename__ = 'posts'

   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String, nullable=False)
   content = db.Column(db.String, nullable=False)
   image = db.Column(db.String, default='post.jpg')
   time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
 #  writer = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
   comments = db.relationship('Comments', backref='parent_post', lazy=True)
   link = db.Column(db.String, nullable=False, unique=True)
   user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

   def save_post(self):
      '''
      Adds and commits post instance to database
      db.session.add(post)
      db.session.commit()
      '''
      db.session.add(self)
      db.session.commit()

   def delete_post(self):
      '''
      Deletes and commits post instance from database
      db.session.add(post)
      db.session.commit()
      '''
      db.session.delete(self)
      db.session.commit()

   def __repr__(self):
      return f"Posts('{self.title}', '{self.content}', '{self.time}')"

   @classmethod
   def get_post(cls,art_link):
      post = Posts.query.filter_by(link=art_link).first()
      return post


class Subscriptions(db.Model):

   __tablename__ = 'subscriptions'
   id = db.Column(db.Integer, primary_key=True)
   email = db.Column(db.String(60), nullable=False, unique=True)

   def save_sub(self):
      '''
      Adds and commits subscription email instance to database
      db.session.add(subscription)
      db.session.commit()
      '''
      db.session.add(self)
      db.session.commit()

   def __repr__(self):
      return f"Subscriptions('{self.email}')"


class Comments(db.Model):
   
   __tablename__ = 'comments'
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(60), nullable=False) 
   comment = db.Column(db.String(480), nullable=False)
   posted_on = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

   def save_comment(self):
      '''
      Adds and commits comment instance to database
      db.session.add(comment)
      db.session.commit()
      '''
      db.session.add(self)
      db.session.commit()

   def delete_comment(self):
      '''
      Deletes and commits comment instance from database
      db.session.add(comment)
      db.session.commit()
      '''
      db.session.delete(self)
      db.session.commit()

   def __repr__(self):
      return f"Comments('{self.comment}')"


@login_manager.user_loader
def load_user(user_id):
   return Users.query.get(int(user_id))
   