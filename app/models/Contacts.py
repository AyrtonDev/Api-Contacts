import uuid
from app import db
from sqlalchemy.dialects.postgresql import UUID

class Contacts(db.Model):
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    category_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=True)
