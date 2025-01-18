from fastapi import FastAPI
from sqlalchemy.orm import Session
from route import router
from database import engine, SessionLocal
import model
from database import engine
from auth import get_password_hash
import uvicorn

# Set up DB and router
model.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router, tags=["books"])


def create_dummy_user():
    """Creates a dummy user for testing."""
    db: Session = SessionLocal()
    try:
        username = "dummyuser"
        password = "dummypassword"

        user = db.query(model.User).filter(model.User.username == username).first()
        if not user:
            hashed_password = get_password_hash(password)
            new_user = model.User(username=username, password=hashed_password)
            db.add(new_user)
            db.commit()
            print(f"Dummy user '{username}' created with password '{password}'.")
        else:
            print(f"Dummy user '{username}' already exists.")
    except Exception as e:
        print(f"Error creating dummy user: {e}")
    finally:
        db.close()


@app.on_event("startup")
def startup_event():
    create_dummy_user()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
