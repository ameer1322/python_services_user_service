from datetime import date
from typing import Optional

from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    email: str
    age: int
    join_date: Optional[date] = None
    address: str
    is_registered: bool

    # id INT NOT NULL AUTO_INCREMENT,
    # first_name VARCHAR(255) NOT NULL DEFAULT "",
    # last_name VARCHAR(255) NOT NULL DEFAULT "",
    # email VARCHAR(255) NOT NULL UNIQUE,
    # age INT NOT NULL,
    # address VARCHAR(255),
    # join_date DATE DEFAULT CURRENT_DATE,
    # is_registered BOOL DEFAULT FALSE