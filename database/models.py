from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Float, BigInteger
from sqlalchemy.orm import relationship

from database import Base


# Таблица пользователей
class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    user_city = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    password = Column(String)
    reg_date = Column(DateTime)
    

# Таблица постов
class UserPost(Base):
    __tablename__ = 'users_posts'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    main_text = Column(String, nullable=False)
    user_id = Column(BigInteger, ForeignKey('users.id'))
    reg_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')

# Таблица фото
class UserPhoto(Base):
    __tablename__ = 'users_photos'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    post_id = Column(BigInteger, ForeignKey('users_posts.id'))
    photo_path = Column(String, nullable=False)

    post_fk = relationship(User, lazy='subquery')

# Таблица хэштегов
class Hashtag(Base):
    __tablename__ = 'hashtags'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    hashtag_name = Column(String, nullable=False, unique=True)
    post_id = Column(BigInteger, ForeignKey('users_posts.id'))
    reg_date = Column(DateTime)

    post_fk = relationship(UserPost, lazy='subquery')

# Таблица комментов
class Comment(Base):
    __tablename__ = 'comments'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    post_id = Column(BigInteger, ForeignKey('users_posts.id'))
    user_id = Column(BigInteger, ForeignKey('users.id'))
    comment_text = Column(String, nullable=False, unique=True)
    reg_date = Column(DateTime)

    post_fk = relationship(UserPost, lazy='subquery')
    user_fk = relationship(User, lazy='subquery')