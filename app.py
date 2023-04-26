from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from PIL import Image
import numpy as np
import cv2
import tempfile
from datetime import datetime
from pilot_model import pilot_model
#from fastapi.responses import HTMLResponse
#from fastapi.templating import Jinja2Templates

app = FastAPI()

# Добавляем middleware для CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Rostelecom": "Tree_Segmentation"}


@app.get("/date")
async def get_current_date():
    return {"date": datetime.now().date()}


@app.get("/power")
def power(x: int=25, y: int=2):
    return [x, y, x**y]


# Обработка изображения
@app.post("/process_image")
async def process_image(image: UploadFile = File(...)):
    # Загрузка изображения из запроса
    image_data = await image.read()
    pil_image = Image.open(BytesIO(image_data))

    # Обработка изображения с помощью функции pilot_model
    result = pilot_model(pil_image)

    # Сохранение результата во временный файл
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        cv2.imwrite(temp_file.name, result)

        # Отправка результата обратно клиенту
        return FileResponse(temp_file.name, media_type="image/png", headers={"Content-Disposition": f"attachment; filename={image.filename}_processed.png"})

