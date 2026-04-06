from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.core.database import get_db
from src.models.models import Record, User
from src.schemas.schemas import RecordCreate, RecordResponse

router = APIRouter(prefix="/records", tags=["Finance Records"])

@router.post("/", response_model=RecordResponse, status_code=status.HTTP_201_CREATED)
def create_record(record_data: RecordCreate, user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    new_record = Record(user_id=user_id, **record_data.dict())
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

@router.get("/user/{user_id}", response_model=List[RecordResponse])
def get_user_records(user_id: int, db: Session = Depends(get_db)):
    return db.query(Record).filter(Record.user_id == user_id).all()

@router.put("/{record_id}", response_model=RecordResponse)
def update_record(record_id: int, updated_data: RecordCreate, db: Session = Depends(get_db)):
    db_record = db.query(Record).filter(Record.id == record_id).first()
    if not db_record:
        raise HTTPException(status_code=404, detail="Record not found")
    for key, value in updated_data.dict().items():
        setattr(db_record, key, value)
    db.commit()
    db.refresh(db_record)
    return db_record

@router.delete("/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_record(record_id: int, db: Session = Depends(get_db)):
    record = db.query(Record).filter(Record.id == record_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    db.delete(record)
    db.commit()
    return None

@router.get("/user/{user_id}/summary")
def get_user_summary(user_id: int, db: Session = Depends(get_db)):
    records = db.query(Record).filter(Record.user_id == user_id).all()
    total_income = sum(r.amount for r in records if r.type == "income")
    total_expense = sum(r.amount for r in records if r.type == "expense")
    balance = total_income - total_expense
    return {
        "user_id": user_id,
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "transaction_count": len(records)
    }