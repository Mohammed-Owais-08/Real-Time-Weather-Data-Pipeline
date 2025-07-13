API_KEY='dc86869ebbb9b790c93864f3974ffb2c'
import os
from sqlalchemy import create_engine

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///weather.db")
engine = create_engine(DATABASE_URL)
