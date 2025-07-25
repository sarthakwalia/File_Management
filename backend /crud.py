from fastapi import UploadFile
from models import FileRecord
from database import engine
from sqlmodel import Session, select
import shutil
import os

UPLOAD_FOLDER = "uploads"

async def save_file(file: UploadFile):
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    record = FileRecord(
        filename=file.filename,
        filetype=file.content_type,
        filesize=os.path.getsize(file_location)
    )
    with Session(engine) as db:
        db.add(record)
        db.commit()
        db.refresh(record)
    return {"message": "File uploaded", "id": record.id}


def list_files():
    with Session(engine) as db:
        return db.exec(select(FileRecord)).all()


def get_file_by_id(file_id: int):
    with Session(engine) as db:
        return db.get(FileRecord, file_id)
