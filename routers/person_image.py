from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from database import get_db
from models.person_image import PersonImage
from auth_dependency import get_current_user


router = APIRouter(
    prefix="/api/person-images",
    tags=["Person Images"]
)


@router.post("/")
def create_person_image(
    person_id: UUID = None,
    detection_id: UUID = None,
    image_path: str = "",
    image_type: str = "EVIDENCE",
    mime_type: str = "image/jpeg",
    file_size_bytes: int = None,
    sha256_hash: str = None,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    image = PersonImage(
        person_id=person_id,
        detection_id=detection_id,
        image_path=image_path,
        image_type=image_type,
        mime_type=mime_type,
        file_size_bytes=file_size_bytes,
        sha256_hash=sha256_hash
    )

    db.add(image)
    db.commit()
    db.refresh(image)

    return {
        "message": "Person image created successfully",
        "image_id": image.id
    }


@router.get("/")
def get_person_images(
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    return db.query(PersonImage).all()