from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item, User
# from flask import url_for

engine = create_engine('sqlite:///items.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy users
user1 = User(name="John Doe", email="emailjohn@example.com",
             picture='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/User_with_smile.svg/2000px-User_with_smile.svg.png') # noqa
session.add(user1)
session.commit()

user2 = User(name="Jane Doe", email="emailjane@example.com",
             picture='https://upload.wikimedia.org/wikipedia/commons/9/98/User-female.svg')  # noqa
session.add(user2)
session.commit()

# Create categoryies
category1 = Category(
    id="1",
    name="Adventure",
    image="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Members_of_SOCP_conduct_a_free-fall_parachute_training_jump.jpg/731px-Members_of_SOCP_conduct_a_free-fall_parachute_training_jump.jpg",  # noqa
    user_id=1)
session.add(category1)
session.commit()

category2 = Category(
    id="2",
    name="Travel",
    image="https://c1.staticflickr.com/5/4049/4656741826_3ded52ae36_b.jpg",  # noqa
    user_id=1)
session.add(category2)
session.commit()

category3 = Category(
    id="3",
    name="Culture",
    image="https://upload.wikimedia.org/wikipedia/commons/d/db/King_Midas_(rockband)_concert_1.jpg",  # noqa
    user_id=1)
session.add(category3)
session.commit()

# Create Items
item1 = Item(
    name="free fall",
    description="",
    date="in 2016",
    image="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Members_of_SOCP_conduct_a_free-fall_parachute_training_jump.jpg/731px-Members_of_SOCP_conduct_a_free-fall_parachute_training_jump.jpg",  # noqa
    category_id=category1.id,
    user_id=1)
session.add(item1)
session.commit()

item2 = Item(
    name="Concert Madonna",
    description="",
    date="before 2017",
    image="https://upload.wikimedia.org/wikipedia/commons/5/5c/Madonna_02837291_29281_Milan.jpg",  # noqa
    category_id=category3.id,
    user_id=1)
session.add(item2)
session.commit()

item3 = Item(
    name="Visit Argentina",
    description="",
    date="before 2020",
    image="https://upload.wikimedia.org/wikipedia/commons/0/0c/The_World_Factbook_-_Argentina_-_Flickr_-_The_Central_Intelligence_Agency_(7).jpg",  # noqa
    category_id=category2.id,
    user_id=1)
session.add(item3)
session.commit()

print "Items added!"
