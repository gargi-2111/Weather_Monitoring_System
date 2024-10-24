
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config

Base = declarative_base()

class DailySummary(Base):
    __tablename__ = 'daily_summaries'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    avg_temp = Column(Float)
    max_temp = Column(Float)
    min_temp = Column(Float)
    avg_humidity = Column(Float)  # Added avg humidity
    avg_wind_speed = Column(Float)  # Added avg wind speed
    dominant_condition = Column(String)
    date = Column(DateTime)

def initialize_db():
    engine = create_engine(config.DATABASE_URI)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)

def store_daily_summary(summary):
    session = initialize_db()()
    new_summary = DailySummary(**summary)
    session.add(new_summary)
    session.commit()
    session.close()
