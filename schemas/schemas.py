from typing import Optional

from pydantic import BaseModel


class AccountSchema(BaseModel):
    user_id: Optional[str]
    name: Optional[str]
    surname: Optional[str]
    email: Optional[str]


class LocationSchema(BaseModel):
    time_zone: Optional[str]
    country: Optional[str]
    street: Optional[str]
    apt_suite: Optional[int]
    city: Optional[str]
    state_province: Optional[str]
    zipcode: Optional[int]
    country_code: Optional[int]
    phone: Optional[int]
