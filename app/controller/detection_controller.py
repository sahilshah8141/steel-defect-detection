from fastapi import APIRouter
from fastapi import File, UploadFile
from app.services.detection_services import AppServices, DetectionServices
from app.request_models.detection_model import DetectionModel
from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow as tf

detection_router = APIRouter()
image_shape = (256, 1600, 3)


@detection_router.post('/')
async def defect_detection(detection_details: DetectionModel):
    """
    This API is used to detect the steel defect based on the user input.
    ...
    Author
    --------------
    Name: Sahil Shah
    """

    print(detection_details)
    detection_res = DetectionServices.defect_detection_service(detection_details.image_url)
    response = AppServices.app_response(200, "Steel defect detection procedure completed"
                                             " successfully!!", detection_res)

    return response

