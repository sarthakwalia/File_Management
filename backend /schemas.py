from pydantic import BaseModel
from typing import Optional

class FileResponseSchema(BaseModel):
    id: int
    filename: str
    filetype: str
    filesize: int
    content: Optional[str] = None
