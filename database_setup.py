import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    image = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        # Returns objec data in easily serializeable format
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id,
        }


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(Text, nullable=True)
    date = Column(String(8))
    image = Column(Text, nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        # Returns objec data in easily serializeable format
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date': self.date,
            'occasion': self.occasion,
            'image': self.image,
            'category_id': self.category_id,
            'user_id': self.user_id,
        }

# insert at end of file
engine = create_engine('sqlite:///items.db')

Base.metadata.create_all(engine)
