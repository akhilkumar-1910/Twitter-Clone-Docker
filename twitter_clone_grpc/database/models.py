import datetime
import uuid

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(100))
    email = Column(String(50))
    password = Column(String())
    userprofile = relationship(
        "UserProfile",
        uselist=False,
        back_populates="user",
        cascade="all, delete, delete-orphan",
    )

    def __str__(self):
        return f"{self.uuid} -> {self.username}:{self.email}"


class UserProfile(Base):
    __tablename__ = "userprofile"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.uuid", ondelete="CASCADE"))
    user = relationship("User", back_populates="userprofile")
    mobile_number = Column(String(20))

    def __str__(self):
        return f"{self.uuid} -> user_id: {self.user_id}"


class Tweet(Base):
    __tablename__ = "tweet"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.uuid", ondelete="CASCADE"))
    content = Column(String(200))
    posted_at = Column(DateTime, default=datetime.datetime.now)
    last_edited_at = Column(DateTime, onupdate=datetime.datetime.now)
    tags = relationship(
        "Tag", back_populates="tweet", cascade="all, delete, delete-orphan"
    )

    def __str__(self):
        return f"{self.uuid}.{self.user_id} -> {self.content}"


class Tag(Base):
    __tablename__ = "tag"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tag = Column(String(50))
    tweet_id = Column(UUID(as_uuid=True), ForeignKey("tweet.uuid", ondelete="CASCADE"))
    tweet = relationship("Tweet", back_populates="tags")

    def __str__(self):
        return f"{self.uuid} -> {self.tweet_id}: {self.tag}"
