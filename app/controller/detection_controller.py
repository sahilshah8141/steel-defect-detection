from fastapi import APIRouter
from fastapi import File, UploadFile
from app.services.detection_services import AppServices, DetectionServices
from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow as tf

detection_router = APIRouter()
image_shape = (256, 1600, 3)


def load_image_into_numpy_array(data):
    numpy_data = np.array(Image.open(BytesIO(data)))
    data = tf.convert_to_tensor(numpy_data, dtype=tf.float32)
    user_image = tf.image.convert_image_dtype(data, tf.float32)
    user_image = tf.image.resize(user_image, image_shape[:-1])
    return user_image.numpy()


@detection_router.post('/')
async def defect_detection(file: UploadFile = File(...)):
    """
    This API is used to detect the steel defect based on the user input.
    ...
    Author
    --------------
    Name: Sahil Shah
    """

    extension = file.filename.split(".")[-1].lower() in ("jpg", "jpeg", "png")

    if not extension:
        response = AppServices.app_response(500, "Image must be jpg or png format!",
                                            "Internal Server Error")
    else:
        image = load_image_into_numpy_array(await file.read())
        detection_res = DetectionServices.defect_detection_service(image)
        response = AppServices.app_response(200, "Steel defect detection procedure completed"
                                                 " successfully!!", detection_res)

    return response

