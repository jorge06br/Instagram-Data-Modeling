import os
import sys
from sqlalchemy import Column,ForeignKey,Integer,String,Table,Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

follower=Table('followers',Base.metadata,   
    Column('User_from_id',Integer,ForeignKey('user.id')),
    Column('User_to_id',Integer,ForeignKey('user.id'))
)

class User(Base):
    __tablename__ ="user"
    id = Column(Integer,primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(50))
    posts = relationship("Post",backref='Posts')

class Post(Base):
    __tablename__='post'
    id = Column(Integer,primary_key=True)
    user_id =Column(Integer,ForeignKey('user.id'))

class Media(Base):
    __tablename__='media'
    id=Column(Integer,primary_key=True)
    types=Column(Enum)
    url=Column(String(250))
    post_id=Column(Integer,ForeignKey('post.id'))

class Comment(Base):
    __tablename__='comment'
    id=Column(Integer,primary_key=True)
    text=Column(String(250))
    user_id=Column(Integer,ForeignKey('user.id'))
    post_id=Column(Integer,ForeignKey('post.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e