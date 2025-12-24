from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Users(BaseModel):
    email: Optional[str]=None
    password_hash: Optional[str]=None
    full_name: Optional[str]=None
    role: Optional[str]=None
    wishlist_note: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadUsers(BaseModel):
    email: Optional[str]=None
    password_hash: Optional[str]=None
    full_name: Optional[str]=None
    role: Optional[str]=None
    wishlist_note: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class ExchangeEvents(BaseModel):
    name: Optional[str]=None
    budget_limit: Optional[float]=None
    exchange_date_dt: Optional[Any]=None
    is_drawn: Optional[int]=None
    created_at_dt: Optional[Any]=None


class ReadExchangeEvents(BaseModel):
    name: Optional[str]=None
    budget_limit: Optional[float]=None
    exchange_date_dt: Optional[Any]=None
    is_drawn: Optional[int]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class Assignments(BaseModel):
    event_id: Optional[int]=None
    santa_user_id: Optional[int]=None
    recipient_user_id: Optional[int]=None
    created_at_dt: Optional[Any]=None


class ReadAssignments(BaseModel):
    event_id: Optional[int]=None
    santa_user_id: Optional[int]=None
    recipient_user_id: Optional[int]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    email: Optional[str]=None
    password_hash: Optional[str]=None
    full_name: Optional[str]=None
    role: Optional[str]=None
    wishlist_note: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutAssignmentsId(BaseModel):
    id: int = Field(...)
    event_id: Optional[int]=None
    santa_user_id: Optional[int]=None
    recipient_user_id: Optional[int]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostAssignments(BaseModel):
    event_id: Optional[int]=None
    santa_user_id: Optional[int]=None
    recipient_user_id: Optional[int]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostExchangeEvents(BaseModel):
    name: Optional[str]=None
    budget_limit: Optional[Any]=None
    exchange_date_dt: Optional[str]=None
    is_drawn: Optional[int]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutExchangeEventsId(BaseModel):
    id: int = Field(...)
    name: Optional[str]=None
    budget_limit: Optional[Any]=None
    exchange_date_dt: Optional[str]=None
    is_drawn: Optional[int]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: int = Field(...)
    email: Optional[str]=None
    password_hash: Optional[str]=None
    full_name: Optional[str]=None
    role: Optional[str]=None
    wishlist_note: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



# Query Parameter Validation Schemas

class DeleteUsersIdQueryParams(BaseModel):
    """Query parameter validation for delete_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetExchangeEventsIdQueryParams(BaseModel):
    """Query parameter validation for get_exchange_events_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetUsersIdQueryParams(BaseModel):
    """Query parameter validation for get_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteExchangeEventsIdQueryParams(BaseModel):
    """Query parameter validation for delete_exchange_events_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteAssignmentsIdQueryParams(BaseModel):
    """Query parameter validation for delete_assignments_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetAssignmentsIdQueryParams(BaseModel):
    """Query parameter validation for get_assignments_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True
