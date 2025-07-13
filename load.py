from sqlalchemy import create_engine,Column,String,Float,Integer,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base= declarative_base()

class Weather(Base):
    __tablename__='weather_data'
    id=Column(Integer,primary_key=True)
    city=Column(String)
    temperature = Column(Float)
    humidity = Column(Integer)
    wind_speed = Column(Float)
    weather = Column(String)
    timestamp = Column(DateTime)

def save_to_db(data,db_url="sqlite:///weather.db"):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    record = Weather(
        city=data["city"],
        temperature=data["temperature"],
        humidity=data["humidity"],
        wind_speed=data["wind_speed"],
        weather=data["weather"],
        timestamp=datetime.strptime(data["timestamp"], '%Y-%m-%d %H:%M:%S')
    )

    session.add(record)
    session.commit()
    session.close()
    print("✅ Data saved to database.")