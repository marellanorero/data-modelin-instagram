import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

association_share_post= Table(
    "share_post_post",
    Base.metadata,
    Column("post_id", ForeignKey("post.id")),
    Column("share_post_id", ForeignKey("share_post.id")),
)

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50))
    post = relationship("Post", back_populates="person")

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    contenido = Column(String(250))
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", back_populates="post")
    liked_post = relationship("Liked_Post", back_populates="post")
    saved_post = relationship("Saved_Post", back_populates="post")
    share_post = relationship("Share_Post", secondary=association_share_post, back_populates="post")

class Liked_Post(Base):
    __tablename__ = 'liked_post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post", back_populates="liked_post")

class Saved_Post(Base):
    __tablename__= 'saved_post'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post", back_populates="saved_post")

class Share_Post(Base):
    __tablename__ = 'share_post'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    post = relationship(
        "Post", secondary=association_share_post, back_populates="saved_post"
    )

    def to_dict(self):
        return {}




## tabla compartir, relacionada con post ... un post puede compartirse muchas veces, muchos a uno uno a muchos, ver resultado y detallar con comentario antes de enviar terminado

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e