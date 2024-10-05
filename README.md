전송 파일 형식

data={
        "process": 프로세스 번호(int),
        "images": [
        {"image_name": 이미지 이름1, "image_data": Base64로 인코드 된 이미지1},
        {"image_name": 이미지 이름2, "image_data": Base64로 인코드 된 이미지2},
        {"image_name": 이미지 이름3, "image_data": Base64로 인코드 된 이미지3}
    ]
    }


전송 url
url = "http://127.0.0.1:8000/upload_images"
