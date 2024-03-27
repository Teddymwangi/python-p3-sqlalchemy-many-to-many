from models import Base, Game, User, Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///many_to_many.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add your seeding logic here

session.commit()
from models import Base, Game, User, Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///many_to_many.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add your seeding logic here

session.commit()
