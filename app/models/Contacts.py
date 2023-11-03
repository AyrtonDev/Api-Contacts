import uuid
from app import db
from sqlalchemy.dialects.postgresql import UUID
from typing import Optional

class ContactProps:
    def __init__(self, id: Optional[str | uuid.UUID], name: str, phone: str, email:str, category_id:str | uuid.UUID):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.category_id = category_id


class Contacts(db.Model):
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    category_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=True)
