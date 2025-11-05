from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
db_url = f"mysql+pymysql://{os.getenv('dbuser')}:{os.getenv('dbpassword')}@{os.getenv('dbhost')}:{os.getenv('dbport')}/{os.getenv('dbname')}"
engine = create_engine(
    db_url
)

session = sessionmaker(bind=engine)
db = session()

create_users_table = text("""
CREATE TABLE IF NOT EXISTS users_table(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL,
password VARCHAR(100) NOT NULL
)                       
                          """)

db.execute(create_users_table)
print("Users table created successfully")