from typing import Optional

from pydantic import BaseModel


class AccountSchema(BaseModel):
    user_id: Optional[str]
    name: Optional[str]
    surname: Optional[str]
    email: Optional[str]
