import os
from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Dynamically choose DB
db_url = os.getenv("DATABASE_URL", "sqlite:///weather.db")
engine = create_engine(db_url)

Base = declarative_base()

class Weather(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    temperature = Column(Float)
    humidity = Column(Integer)
    wind_speed = Column(Float)
    weather = Column(String)
    timestamp = Column(DateTime)
    date=Column(DateTime)

# Ensure tables are created once
Base.metadata.create_all(engine)

def save_to_db(data):
    Session = sessionmaker(bind=engine)
    session = Session()
    dat=datetime.now()
    record = Weather(
        city=data["city"],
        temperature=data["temperature"],
        humidity=data["humidity"],
        wind_speed=data["wind_speed"],
        weather=data["weather"],
        timestamp=datetime.strptime(data["timestamp"], '%Y-%m-%d %H:%M:%S'),
        date=dat
    )

    session.add(record)
    session.commit()
    session.close()
    print("✅ Data saved to database.")
