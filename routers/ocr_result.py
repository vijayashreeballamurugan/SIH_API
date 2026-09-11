from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from database import get_db
from models.ocr_result import OCRResult
from auth_dependency import get_current_user

router = APIRouter(
    prefix="/api/ocr-results",
    tags=["OCR Results"]
)


@router.post("/")
def create_ocr_result(
    detection_id: UUID,
    image_id: UUID,
    plate_number: str = None,
    raw_text: str = None,
    confidence: float = None,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    ocr = OCRResult(
        detection_id=detection_id,
        image_id=image_id,
        plate_number=plate_number,
        raw_text=raw_text,
        confidence=confidence
    )

    db.add(ocr)
    db.commit()
    db.refresh(ocr)

    return {
        "message": "OCR result created successfully",
        "ocr_id": str(ocr.id)
    }


@router.get("/")
def get_ocr_results(
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    results = db.query(OCRResult).all()

    return results


@router.put("/{ocr_id}/verify")
def verify_ocr_result(
    ocr_id: UUID,
    verified_plate_number: str,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    ocr = db.query(OCRResult).filter(OCRResult.id == ocr_id).first()

    if not ocr:
        return {
            "message": "OCR result not found"
        }

    ocr.is_verified = True
    ocr.verified_plate_number = verified_plate_number

    db.commit()
    db.refresh(ocr)

    return {
        "message": "OCR result verified successfully",
        "ocr_id": str(ocr.id),
        "verified_plate_number": ocr.verified_plate_number,
        "is_verified": ocr.is_verified
    }