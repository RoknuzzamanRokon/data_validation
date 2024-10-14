from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

# Define your base
Base = declarative_base()

# Define the connection parameters based on your config
host = '127.0.0.1'  # Host from config
port = 3306          # Replace with the actual port number
user = 'root'       # User from config
password = ''       # Password from config (empty in your case)
database = 'testdb' # Specify your database name

# Create the database URL
database_url = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'

# Create the SQLAlchemy engine
engine = create_engine(database_url)

# Example User class for ORM
class User(Base):
    __tablename__ = 'users'  
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

Base.metadata.create_all(engine)

print("Database connection established and tables created (if they did not exist).")

