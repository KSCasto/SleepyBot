import aiohttp
import os, io

async def send_zip(zipFile):
    url=os.getenv('CM_URL')+"makeCards"

    headersList = {
        "Accept": "*/*",
        "UID": "1077060107264852069",
        "Authorization": "Bearer test_token"
    }

    data = aiohttp.FormData()
    data.add_field('file', zipFile, filename='file.zip', content_type='application/zip')

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headersList, data=data) as response:
            res =  await response.read()
            res = io.BytesIO(res) 
            res.seek(0)
            return res
            