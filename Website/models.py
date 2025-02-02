from . import db   
from flask_login import UserMixin
from sqlalchemy.sql import func  #for fetching the current timestamp for posting 
from flask_login import current_user

#This Function is for Fetching the current user
def get_user_id():
    return current_user.id if current_user.is_authenticated else None



#creating a Post Schema model for storing post information
class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    userId=db.Column(db.Integer, db.ForeignKey('user.id'))
    title=db.Column(db.String(1000))
    content=db.Column(db.Text)
    date=db.Column(db.DateTime(timezone='Australia/Perth'), default=func.date(func.now()))
    
#creating a User Schema model for storing users information 
class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    firstName=db.Column(db.String(150))
    lastName=db.Column(db.String(150))
    emailAddress=db.Column(db.String(254),unique=True)
    password=db.Column(db.String(150))
    posts=db.relationship('Post')

#Creating a Likes Schema Model for storing like interactions on post by Users
class Likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    postId = db.Column(db.Integer, db.ForeignKey('post.id'))
    userId = db.Column(db.Integer, default=get_user_id)
 
#Creating a Comments Schema Model for Storing Comments by Users
class Comments(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    postId=db.Column(db.Integer, db.ForeignKey('post.id'))
    content=db.Column(db.Text)
    date=db.Column(db.DateTime(timezone='Australia/Perth'), default=func.date(func.now()))
#Creating a Reply Schema Model for storing Replies by Users
class Reply(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    commentId=db.Column(db.Integer, db.ForeignKey('comments.id'))
    content=db.Column(db.Text)
    date=db.Column(db.DateTime(timezone='Australia/Perth'), default=func.date(func.now()))
    repliedBy=db.Column(db.Text)
    repliedTo=db.Column(db.Text)
    postId=db.Column(db.Integer)
    userId=db.Column(db.Integer)
#Creating a Comments Like Schema for storing like interactions on Comments by Users
class CommentsLike(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    commentId=db.Column(db.Integer, db.ForeignKey('comments.id'))
    userId=db.Column(db.Integer)
    
    


    

