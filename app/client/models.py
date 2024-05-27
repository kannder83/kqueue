import datetime
from pydantic import BaseModel, EmailStr
from mongoengine import Document, StringField, DateTimeField, EmailField
from typing import Optional, List


class CreateClient(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]

    def to_dict(self):
        return {
            field: str(getattr(self, field)
                       ) if field == "id" else getattr(self, field)
            for field in self._fields.keys()
        }

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "name",
                "email": "email@example.com",
                "phone": "55555555",
            }
        }
    }


class Client(Document):
    name = StringField(max_length=200, required=True)
    email = EmailField(max_length=200, required=True)
    phone = StringField(max_length=200, required=True)
    date_modified = DateTimeField(default=datetime.datetime.now)

    def to_dict(self):
        return {
            field: str(getattr(self, field)
                       ) if field == "id" else getattr(self, field)
            for field in self._fields.keys()
        }
