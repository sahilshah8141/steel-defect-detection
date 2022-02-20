import os
from pathlib import Path
from tensorflow.keras.models import load_model
import numpy as np
import skimage.io

project_path = Path(__file__).parent.parent.parent
model_detection_file = os.path.join(project_path, "model/inceptionv3.h5")
image_shape = (256, 1600, 3)
defection_types = ['defect_1', 'defect_2', 'defect_3', 'defect_4']
threshold = 0.99
model = load_model(model_detection_file)


class DetectionServices:

    @staticmethod
    def defect_detection_service(user_image_url):

        try:
            user_img_arr = skimage.io.imread(user_image_url)
            user_img_arr = user_img_arr.reshape((1,) + image_shape)
            detection_res = model.predict(user_img_arr)
            detection_res = np.where(detection_res > threshold, 1, 0).tolist()[0]
            detected_defects = detection_res.count(1)

            if detected_defects:
                if detected_defects == 1:
                    detection_res = "Feeling sad!! This steel sheet image is defective and it has 1 type of defect."
                else:
                    detection_res = "Feeling sad!! This steel sheet image is defective" \
                                    " and it has total {} types of defects.".format(detected_defects)
            else:
                detection_res = "Cheer up!! This steel sheet image isn't defective ."

        except Exception as v_exc:
            detection_res = v_exc.__str__()

        return detection_res


class AppServices:

    @staticmethod
    def app_response(status_code: int, message: str, data: any = None) -> dict:
        response = {
            "status_code": status_code,
            "message": message,
            "data": data
        }
        return response



