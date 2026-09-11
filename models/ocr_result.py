from sqlalchemy import Column, String, DateTime, Boolean, Text, ForeignKey, Numeric, text
from sqlalchemy.dialects.postgresql import UUID
from database import Base


class OCRResult(Base):
    __tablename__ = "ocr_results"

    id = Column(
        "ocr_id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    detection_id = Column(
        UUID(as_uuid=True),
        ForeignKey("detections.detection_id", ondelete="CASCADE"),
        nullable=False
    )

    image_id = Column(
        UUID(as_uuid=True),
        ForeignKey("person_images.image_id", ondelete="CASCADE"),
        nullable=False
    )

    plate_number = Column(
        String(20),
        nullable=True
    )

    raw_text = Column(
        Text,
        nullable=True
    )

    confidence = Column(
    Numeric(5, 2),
    nullable=True
    )
    

    is_verified = Column(
        Boolean,
        nullable=False,
        server_default=text("FALSE")
    )

    verified_plate_number = Column(
        String(20),
        nullable=True
    )

    processed_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    )

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    )