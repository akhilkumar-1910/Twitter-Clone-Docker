from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime


Base = declarative_base()


class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    content = Column(String(200))
    posted_at = Column(DateTime, default=datetime.datetime.now)
    last_edited_at = Column(DateTime, onupdate=datetime.datetime.now)
    tags = relationship("Tag", back_populates="tweet", cascade="all, delete, delete-orphan")

    def __str__(self):
        return f"{self.id}. {self.content}"


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    tag = Column(String(50))
    tweet_id = Column(Integer, ForeignKey('tweets.id', ondelete='CASCADE'))
    tweet = relationship("Tweet", back_populates="tags")

    def __str__(self):
        return f"{self.id}. {self.tag}"
