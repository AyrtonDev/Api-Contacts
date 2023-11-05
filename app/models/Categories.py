import uuid
from app import db
from sqlalchemy.dialects.postgresql import UUID

class Categories(db.Model):
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
