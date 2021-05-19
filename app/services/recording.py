import logging

import requests

from config import TRANSCRIPTION_BASE_URL


logger = logging.getLogger()

class Recording:
    def transcribe(recording_url):
        text = None

        url = f"{TRANSCRIPTION_BASE_URL}/transcribe"
        data = {"recording_url": recording_url}
        response = requests.post(url=url, data=data)

        if response.ok:
            json = response.json()

            if "text" in json:
                text = json["text"]

        return text
