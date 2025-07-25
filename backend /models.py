from sqlmodel import SQLModel, Field
from typing import Optional

class FileRecord(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    filename: str
    filetype: str
    filesize: int
