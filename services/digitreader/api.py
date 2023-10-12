from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import uvicorn
import time
from keras import models
from PIL import Image
import numpy
import os
model = models.load_model('handwriting.keras')

app = FastAPI()


@app.get('/')
async def getHome():
    return FileResponse('index.html')


@app.post('/images')
async def readImage(req: Request):
    content = await req.body()
    dst = str(time.time())+'.png'
    fo = open(dst, 'wb')
    fo.write(content)
    fo.close()

    img = numpy.asarray(Image.open(dst), float)
    img = numpy.expand_dims(img, axis=0)
    img = (img/255)-0.5
    img = numpy.expand_dims(img, axis=3)

    predictions = model.predict(img)
    labels = numpy.argmax(predictions)

    os.remove(dst)
    return str(labels)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
