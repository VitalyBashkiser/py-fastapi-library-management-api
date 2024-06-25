from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Author(Base):
    __tablename__ = "authors"

    id_ = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    bio = Column(String)

    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"

    id_ = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    summary = Column(String)
    publication_date = Column(Date)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")