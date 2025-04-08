from sqlalchemy import Column , Integer, String, create_engine
from sqlalchemy.orm import declarative_base , sessionmaker

Base = declarative_base()

class BookingDB(Base):
    __tablename__ = "Books"

    id = Column(Integer, primary_key=True)
    Título = Column(String),
    Price = Integer,
    availability = Column(String),
    description = Column(String)

engine = create_engine('sqlite:///../database/BookingDB.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine) 

