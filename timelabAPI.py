# -*- coding: utf-8 -*-
# 実行して確認するためには「uvicornのインストール」と「ターミナルで uvicorn fastAPI:app --reload をうつ」が必要
from fastapi import FastAPI   # 外部ライブラリ
import cv2
import json   # 標準ライブラリ
import timeLabQrCode   # 自作ライブラリ

app = FastAPI()

@app.get("/createQrCode/{roomId}")
async def createQrCode(roomId):

    imageCv2 = timeLabQrCode.roomIdToPngQrCode(roomId)   # base64に変換するとき OpneCv型 である必要あり
    imageBase64 = timeLabQrCode.pngEncodeToBase64(imageCv2)

    return {"imageBase64": imageBase64}   # 自動でjson形式になる