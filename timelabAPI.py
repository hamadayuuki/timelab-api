# -*- coding: utf-8 -*-
# 実行して確認するためには「uvicornのインストール」と「ターミナルで uvicorn fastAPI:app --reload をうつ」が必要
from fastapi import FastAPI   # 外部ライブラリ
import cv2
import json   # 標準ライブラリ
import timeLabQrCode   # 自作ライブラリ

app = FastAPI()

@app.get("/createQrCode/{roomId}")
async def createQrCode(roomId):

    imageCv2 = timeLabQrCode.roomIdToPngQrCode(roomId)
    print("timelabAPI: type(imageCv2): ", type(imageCv2))
    print("timelabAPI, imageCv2の直後")
    imageBase64 = timeLabQrCode.pngEncodeToBase64(imageCv2)
    print("timelabAPI, imgBase64の直後")

    return {"imageBase64": imageBase64}   # 自動でjson形式になる