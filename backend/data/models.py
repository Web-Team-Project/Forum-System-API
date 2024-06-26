from pydantic import BaseModel, conint, validator
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Enum
from sqlalchemy.sql import func
from data.base import Base
from data.roles import Roles
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(Roles), default="user")
    votes = relationship("Vote", back_populates="user")
    categories = relationship("CategoryAccess", back_populates="user")


class CreateUserRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class Topic(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    author_id = Column(Integer, ForeignKey("users.id"))
    best_reply_id = Column(Integer, ForeignKey("replies.id"))
    is_locked = Column(Boolean, default=False)
    category = relationship("Category", back_populates="topics")


class CreateTopicRequest(BaseModel):
    title: str
    category_id: int


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_private = Column(Boolean, default=False)
    access_records = relationship("CategoryAccess", back_populates="category")
    is_locked = Column(Boolean, default=False)
    topics = relationship("Topic", back_populates="category")



class CategoryAccess(Base):
    __tablename__ = "category_users"
    category_id = Column(Integer, ForeignKey("categories.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    read_access = Column(Boolean, default=False)
    write_access = Column(Boolean, default=False)
    category = relationship("Category", back_populates="access_records")
    user = relationship("User", back_populates="categories")


class CreateCategoryRequest(BaseModel):
    name: str


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    sent_at = Column(DateTime(timezone=True), server_default=func.now())
    sender_id = Column(Integer, index=True)
    receiver_id = Column(Integer, index=True)
    text = Column(String, index=True)


class CreateMessageRequest(BaseModel):
    text: str
    receiver_id: int


class Reply(Base):
    __tablename__ = "replies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_best_reply = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    topic_id = Column(Integer, ForeignKey("topics.id"))
    votes = relationship("Vote", back_populates="reply")


class CreateReplyRequest(BaseModel):
    content: str
    topic_id: int


class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    reply_id = Column(Integer, ForeignKey("replies.id"), primary_key=True)
    vote_type = Column(Integer)
    user = relationship("User", back_populates="votes")
    reply = relationship("Reply", back_populates="votes")


class CreateVoteRequest(BaseModel):
    vote_type: conint(ge=-1, le=1) # type: ignore

    @validator("vote_type")
    def check_vote_type(cls, value):
        if value not in (-1, 1):
            raise ValueError("vote_type must be either -1 (downvote) or 1 (upvote).")
        return value