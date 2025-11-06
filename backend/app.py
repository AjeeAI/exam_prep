from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from sqlalchemy import text
from database import db
import bcrypt
import os

load_dotenv()

app = FastAPI(title="Prep backend execution", version="1.0.0")


app.add_middleware(
    CORSMiddleware,
    # allow_origins=[
    #     "http://localhost:5173",  # Vite default
    #     "http://localhost:3000",  # Create React App default
    #     "http://127.0.0.1:5173",
    #     "http://127.0.0.1:3000",
    # ],
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  # allow all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],  # allow all headers (Authorization, Content-Type, etc.)
)


@app.get("/")
def home():
    return "This is my API in preparation for my exam"


class SignUp(BaseModel):
    name: str = Field(..., example="Adesoji Ajijolaoluwa")
    email: str = Field(..., example="ajee@gmail.com")
    password: str = Field(..., example="ajee123")


@app.post("/signup")
def sign_up(input: SignUp):
    try:
        check_query = text("""
            SELECT * FROM users_table
            WHERE email = :email                         
        """)
        existing = db.execute(check_query, {"email": input.email}).fetchone()
        if existing:
            raise HTTPException(
                status_code=400, detail="User already exists! Try logging in instead."
            )

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(input.password.encode("utf-8"), salt)

        add_user_query = text("""
            INSERT INTO users_table(name, email, password)
            VALUES (:name, :email, :password)                
        """)

        db.execute(
            add_user_query,
            {"name": input.name, "email": input.email, "password": hashed_password},
        )
        db.commit()

        return {
            "message": "User added successfully",
            "data": {"name": input.name, "email": input.email},
        }

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class Login(BaseModel):
    email: str = Field(..., example="ajee@gmail.com")
    password: str = Field(..., example="ajee123")


@app.post("/login")
def login(input: Login):
    try:
        login_query = text("""
            SELECT * FROM users_table
            WHERE email = :email             
        """)
        result = db.execute(login_query, {"email": input.email}).mappings().fetchone()

        if not result:
            raise HTTPException(
                status_code=400,
                detail="Invalid email or password. Please check and try again.",
            )

        stored_password = result["password"]

        verified_password = bcrypt.checkpw(
            input.password.encode("utf-8"), stored_password.encode("utf-8")
        )

        if not verified_password:
            raise HTTPException(status_code=401, detail="Invalid email or password")

        return {"message": "Login Successful"}

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/products")

def products():
    try:
        get_products = text("""
SELECT * from products_table
                        """)
        result = db.execute(get_products).mappings().all()
        
        if not result:
            return "No products yet. Try again later."

        return {"products": result}
        
    except HTTPException as e:
        return {"detail": str(e)}
        