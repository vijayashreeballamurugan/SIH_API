from sqlalchemy import Column, String, DateTime, BigInteger, Text, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
from database import Base


class PersonImage(Base):
    __tablename__ = "person_images"

    id = Column(
        "image_id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    person_id = Column(
        UUID(as_uuid=True),
        ForeignKey("persons.person_id", ondelete="SET NULL"),
        nullable=True
    )

    detection_id = Column(
        UUID(as_uuid=True),
        ForeignKey("detections.detection_id", ondelete="SET NULL"),
        nullable=True
    )

    image_path = Column(
        Text,
        nullable=False
    )

    image_type = Column(
        String(30),
        nullable=False
    )

    mime_type = Column(
        String(50),
        nullable=False,
        server_default=text("'image/jpeg'")
    )

    file_size_bytes = Column(
        BigInteger,
        nullable=True
    )

    sha256_hash = Column(
        String(64),
        nullable=True
    )

    captured_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    )

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    )