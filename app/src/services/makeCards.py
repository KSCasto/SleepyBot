import requests
import os

async def send_zip(zipFile):
    url=os.getenv('CM_URL')
    PDF=requests.post(url,files=zipFile)
    return PDF