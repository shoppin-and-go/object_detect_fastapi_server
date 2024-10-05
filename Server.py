from fastapi import FastAPI, Request
import base64
import os

app = FastAPI()

SAVE_DIR = "received_images"
os.makedirs(SAVE_DIR, exist_ok=True)

@app.post("/upload_images")
async def upload_images(request: Request):
    data = await request.json()

    process = data["process"]
    images = data["images"]
    for img in images:
        image_name = img["image_name"]
        image_data = img["image_data"]

        img_bytes = base64.b64decode(image_data)

        with open(os.path.join(SAVE_DIR, image_name), "wb") as f:
            f.write(img_bytes)

    return {"message": f'{process}. 이미지 수신 및 저장 완료!'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

