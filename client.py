import requests

API_URL = "https://ultra-fast-pdf-to-json-bounding-boxes.p.rapidapi.com/parse"

def parse_pdf(file_path, api_key):
    with open(file_path, "rb") as f:
        files = {"file": f}
        headers = {
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": "ultra-fast-pdf-to-json-bounding-boxes.p.rapidapi.com"
        }
        response = requests.post(API_URL, files=files, headers=headers)
        response.raise_for_status()
        return response.json()
