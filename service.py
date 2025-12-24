from sqlalchemy.orm import Session, aliased
from database import SessionLocal
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
from datetime import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


def convert_to_datetime(date_string):
    if date_string is None:
        return datetime.now()
    from fastapi import HTTPException

    if "T" in date_string:
        try:
            return datetime.fromisoformat(date_string.replace("Z", "+00:00"))
        except ValueError:
            date_part = date_string.split("T")[0]
            try:
                return datetime.strptime(date_part, "%Y-%m-%d")
            except ValueError:
                raise HTTPException(
                    status_code=422,
                    detail=f"Improper format in datetime: {date_string}",
                )
    else:
        try:
            return datetime.strptime(date_string, "%Y-%m-%d")
        except ValueError:
            raise HTTPException(
                status_code=422, detail=f"Improper format in datetime: {date_string}"
            )


async def get_exchange_events(db: Session):

    query = db.query(models.ExchangeEvents)

    exchange_events_all = query.all()
    exchange_events_all = (
        [new_data.to_dict() for new_data in exchange_events_all]
        if exchange_events_all
        else exchange_events_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"exchange_events_all": exchange_events_all},
    }
    return res


async def get_users(db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_all": users_all},
    }
    return res


async def get_assignments(db: Session):

    query = db.query(models.Assignments)

    assignments_all = query.all()
    assignments_all = (
        [new_data.to_dict() for new_data in assignments_all]
        if assignments_all
        else assignments_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"assignments_all": assignments_all},
    }
    return res


async def post_users(db: Session, raw_data: schemas.PostUsers):
    email: str = raw_data.email
    password_hash: str = raw_data.password_hash
    full_name: str = raw_data.full_name
    role: str = raw_data.role
    wishlist_note: str = raw_data.wishlist_note
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "role": role,
        "email": email,
        "full_name": full_name,
        "created_at_dt": created_at_dt,
        "password_hash": password_hash,
        "wishlist_note": wishlist_note,
    }
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    # db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_inserted_record": users_inserted_record},
    }
    return res


async def put_assignments_id(db: Session, raw_data: schemas.PutAssignmentsId):
    id: int = raw_data.id
    event_id: int = raw_data.event_id
    santa_user_id: int = raw_data.santa_user_id
    recipient_user_id: int = raw_data.recipient_user_id
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.Assignments)
    query = query.filter(and_(models.Assignments.id == id))
    assignments_edited_record = query.first()

    if assignments_edited_record:
        for key, value in {
            "id": id,
            "event_id": event_id,
            "created_at_dt": created_at_dt,
            "santa_user_id": santa_user_id,
            "recipient_user_id": recipient_user_id,
        }.items():
            setattr(assignments_edited_record, key, value)

        db.commit()

        # db.refresh(assignments_edited_record)

        assignments_edited_record = (
            assignments_edited_record.to_dict()
            if hasattr(assignments_edited_record, "to_dict")
            else vars(assignments_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"assignments_edited_record": assignments_edited_record},
    }
    return res


async def delete_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_deleted": users_deleted},
    }
    return res


async def get_exchange_events_id(db: Session, id: int):

    query = db.query(models.ExchangeEvents)
    query = query.filter(and_(models.ExchangeEvents.id == id))

    exchange_events_one = query.first()

    exchange_events_one = (
        (
            exchange_events_one.to_dict()
            if hasattr(exchange_events_one, "to_dict")
            else vars(exchange_events_one)
        )
        if exchange_events_one
        else exchange_events_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"exchange_events_one": exchange_events_one},
    }
    return res


async def get_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_one": users_one},
    }
    return res


async def delete_exchange_events_id(db: Session, id: int):

    query = db.query(models.ExchangeEvents)
    query = query.filter(and_(models.ExchangeEvents.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        exchange_events_deleted = record_to_delete.to_dict()
    else:
        exchange_events_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"exchange_events_deleted": exchange_events_deleted},
    }
    return res


async def post_assignments(db: Session, raw_data: schemas.PostAssignments):
    event_id: int = raw_data.event_id
    santa_user_id: int = raw_data.santa_user_id
    recipient_user_id: int = raw_data.recipient_user_id
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "event_id": event_id,
        "created_at_dt": created_at_dt,
        "santa_user_id": santa_user_id,
        "recipient_user_id": recipient_user_id,
    }
    new_assignments = models.Assignments(**record_to_be_added)
    db.add(new_assignments)
    db.commit()
    # db.refresh(new_assignments)
    assignments_inserted_record = new_assignments.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"assignments_inserted_record": assignments_inserted_record},
    }
    return res


async def delete_assignments_id(db: Session, id: int):

    query = db.query(models.Assignments)
    query = query.filter(and_(models.Assignments.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        assignments_deleted = record_to_delete.to_dict()
    else:
        assignments_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"assignments_deleted": assignments_deleted},
    }
    return res


async def get_assignments_id(db: Session, id: int):

    query = db.query(models.Assignments)
    query = query.filter(and_(models.Assignments.id == id))

    assignments_one = query.first()

    assignments_one = (
        (
            assignments_one.to_dict()
            if hasattr(assignments_one, "to_dict")
            else vars(assignments_one)
        )
        if assignments_one
        else assignments_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"assignments_one": assignments_one},
    }
    return res


async def post_exchange_events(db: Session, raw_data: schemas.PostExchangeEvents):
    name: str = raw_data.name
    budget_limit: float = raw_data.budget_limit
    exchange_date_dt: str = convert_to_datetime(raw_data.exchange_date_dt)
    is_drawn: int = raw_data.is_drawn
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "name": name,
        "is_drawn": is_drawn,
        "budget_limit": budget_limit,
        "created_at_dt": created_at_dt,
        "exchange_date_dt": exchange_date_dt,
    }
    new_exchange_events = models.ExchangeEvents(**record_to_be_added)
    db.add(new_exchange_events)
    db.commit()
    # db.refresh(new_exchange_events)
    exchange_events_inserted_record = new_exchange_events.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"exchange_events_inserted_record": exchange_events_inserted_record},
    }
    return res


async def put_exchange_events_id(db: Session, raw_data: schemas.PutExchangeEventsId):
    id: int = raw_data.id
    name: str = raw_data.name
    budget_limit: float = raw_data.budget_limit
    exchange_date_dt: str = convert_to_datetime(raw_data.exchange_date_dt)
    is_drawn: int = raw_data.is_drawn
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.ExchangeEvents)
    query = query.filter(and_(models.ExchangeEvents.id == id))
    exchange_events_edited_record = query.first()

    if exchange_events_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "is_drawn": is_drawn,
            "budget_limit": budget_limit,
            "created_at_dt": created_at_dt,
            "exchange_date_dt": exchange_date_dt,
        }.items():
            setattr(exchange_events_edited_record, key, value)

        db.commit()

        # db.refresh(exchange_events_edited_record)

        exchange_events_edited_record = (
            exchange_events_edited_record.to_dict()
            if hasattr(exchange_events_edited_record, "to_dict")
            else vars(exchange_events_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"exchange_events_edited_record": exchange_events_edited_record},
    }
    return res


async def put_users_id(db: Session, raw_data: schemas.PutUsersId):
    id: int = raw_data.id
    email: str = raw_data.email
    password_hash: str = raw_data.password_hash
    full_name: str = raw_data.full_name
    role: str = raw_data.role
    wishlist_note: str = raw_data.wishlist_note
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "id": id,
            "role": role,
            "email": email,
            "full_name": full_name,
            "created_at_dt": created_at_dt,
            "password_hash": password_hash,
            "wishlist_note": wishlist_note,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()

        # db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_edited_record": users_edited_record},
    }
    return res
