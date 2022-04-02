# -*- coding: utf-8 -*-
import qrcode   # 外部ライブラリ
from PIL import Image
import cv2
import numpy as np
import base64   # 標準ライブラリ

# PIL型 -> OpenCV型
def pilToCv2(pilImage):
    cv2Image = np.array(pilImage, dtype=np.uint8)
    if cv2Image.ndim == 2:  # モノクロ
        pass
    elif cv2Image.shape[2] == 3:  # カラー
        cv2Image = cv2.cvtColor(cv2Image, cv2.COLOR_RGB2BGR)
    elif cv2Image.shape[2] == 4:  # 透過
        cv2Image = cv2.cvtColor(cv2Image, cv2.COLOR_RGBA2BGRA)
    return cv2Image


def roomIdToPngQrCode(roomId):
    IMG_SIZE = 1024   # 2^x
    TIMELAB_ICON_SIZE = 200
    TIMELAB_ICON_PATH = "image/TIMELAB_App_Icon.png"
    pngImageName = "TIMELAB_" + roomId + ".png"

    qrCode = qrcode.make(roomId, error_correction = qrcode.constants.ERROR_CORRECT_H).convert('RGB')
    qrCode = qrCode.resize((IMG_SIZE, IMG_SIZE))

    appIcon = Image.open(TIMELAB_ICON_PATH)
    appIcon = appIcon.resize((TIMELAB_ICON_SIZE, TIMELAB_ICON_SIZE))
    qrCode.paste(appIcon, ((IMG_SIZE//2) - (TIMELAB_ICON_SIZE//2), (IMG_SIZE//2) - (TIMELAB_ICON_SIZE//2)))
    # image.save(pngImageName)   # 画像を保存

    qrCodeCv2 = pilToCv2(qrCode)
    print("roomIdToPngQrCode: type(qrCode): ", type(qrCodeCv2))

    return qrCodeCv2


def pngEncodeToBase64(img):
    _, encimg = cv2.imencode(".png", img)
    imgStr = encimg.tostring()
    imgBase64 = base64.b64encode(imgStr).decode("utf-8")
    
    return imgBase64
