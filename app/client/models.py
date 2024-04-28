import datetime
from pydantic import BaseModel
from mongoengine import Document, StringField, DateTimeField
from typing import Optional, List


class CreatePage(BaseModel):
    title: Optional[str]

    def to_dict(self):
        return {
            "title": self.title
        }

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "new title"
            }
        }
    }


class Page(Document):
    title = StringField(max_length=200, required=True)
    date_modified = DateTimeField(default=datetime.datetime.now)

    def to_dict(self):
        return {
            field: str(getattr(self, field)
                       ) if field == "id" else getattr(self, field)
            for field in self._fields.keys()
        }
