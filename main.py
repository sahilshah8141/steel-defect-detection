import uvicorn
from app import get_app
from app.controller.detection_controller import detection_router
from fastapi.templating import Jinja2Templates
from fastapi import Request
import os
from pathlib import Path

project_path = Path(__file__).parent
template_path = os.path.join(project_path, "templates")
templates = Jinja2Templates(directory=template_path)
app = get_app()


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# For Heroku deployment
app.include_router(detection_router, prefix="/detect")

# if __name__ == "__main__":
#     app.include_router(detection_router, prefix="/detect")
#     uvicorn.run(app, host="localhost", port=8007)
