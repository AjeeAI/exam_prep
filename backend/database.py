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

create_products_table = text("""
CREATE TABLE IF NOT EXISTS products_table(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL,
category VARCHAR(255) NOT NULL,
price DECIMAL(10, 2),
quantity INT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);             
                             """)

db.execute(create_products_table)

# add_multiple_products = text("""
# INSERT INTO products_table (name, category, price, quantity) 
# VALUES
# ('Samsung Galaxy S24', 'smartphones', 850000, 12),
# ('Infinix Note 40 Pro', 'smartphones', 310000, 25),
# ('Apple MacBook Air M2', 'laptops', 1250000, 8),
# ('HP Pavilion 15', 'laptops', 620000, 10),
# ('Logitech MX Master 3S Mouse', 'accessories', 85000, 30),
# ('Sony WH-1000XM5', 'headphones', 420000, 15),
# ('JBL Flip 6 Bluetooth Speaker', 'audio', 115000, 20),
# ('LG 55” OLED TV', 'electronics', 980000, 6),
# ('Hisense 2HP Split AC', 'home appliances', 450000, 9),
# ('Philips Air Fryer XXL', 'kitchen', 210000, 14),
# ('Kenwood Food Processor', 'kitchen', 165000, 18),
# ('Nike Air Force 1', 'fashion', 95000, 22),
# ('Adidas Ultraboost 23', 'fashion', 120000, 17),
# ('Samsung 25W Fast Charger', 'accessories', 15000, 40),
# ('Oraimo 10000mAh Power Bank', 'accessories', 22000, 35),
# ('Huawei MatePad 11', 'tablets', 380000, 11),
# ('Apple iPad 10th Gen', 'tablets', 500000, 9),
# ('Seagate 2TB External HDD', 'storage', 78000, 28),
# ('Sandisk 128GB Flash Drive', 'storage', 18000, 45),
# ('Canon EOS 250D DSLR Camera', 'cameras', 650000, 7);
                      
#                              """)

# db.execute(add_multiple_products)
# db.commit()


# delete_rows_query = text("""
# DELETE FROM products_table
# WHERE id >= 21;
     
#                          """)

# db.execute(delete_rows_query)
# db.commit()