from pydantic import BaseModel


class DetectionModel(BaseModel):
    image_url: str
