

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
     "sqlite+libsql:///embedded.db",
     connect_args={
         "sync_url": "libsql://coll-a03848caeeef4dffab94e30930a93285-mayson.aws-ap-south-1.turso.io",
         "auth_token": "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NjY1NzEwMTIsInAiOnsicm9hIjp7Im5zIjpbIjZmMWFlOGVmLTBiODAtNDk4YS04ODE2LTE5ZTg0ZDg4MDU1ZSJdfSwicnciOnsibnMiOlsiNmYxYWU4ZWYtMGI4MC00OThhLTg4MTYtMTllODRkODgwNTVlIl19fSwicmlkIjoiYWVhMTYyMjgtZjgxYy00MGM0LTljMTAtODlhMDQ4YmNhOTg2In0.nK8r-cEFYOWAKT59v5VIbDFzf11dMu7ehwWQy_q1nCbzKFjByOymnUsnsevt6yw1zPkV4YxWyinkGBYTYynfAg",
     },
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
Base = declarative_base()

