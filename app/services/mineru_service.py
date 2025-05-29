import requests
from app.config import settings

MINERU_APPLY_URL = "https://mineru.net/api/v4/file-urls/batch"
MINERU_TASK_RESULT_URL = "https://mineru.net/api/v4/extract-results/batch/{batch_id}"

class MinerUService:
    def __init__(self):
        self.auth_token = settings.MINERU_AUTH_TOKEN
        if not self.auth_token:
            raise ValueError("Missing MINERU_AUTH_TOKEN in environment variables")

    def apply_upload_url(self, filename: str):
        headers = {
            "Authorization": self.auth_token,
            "Content-Type": "application/json",
        }
        data = {
            "enable_formula": True,
            "language": "ch",
            "enable_table": True,
            "files": [{"name": filename}]
        }

        response = requests.post(MINERU_APPLY_URL, json=data, headers=headers)
        result = response.json()

        if result.get("code") != 0:
            raise RuntimeError(f"Apply upload URL failed: {result.get('msg')}")

        return result["data"]["batch_id"], result["data"]["file_urls"][0]

    def upload_file_to_mineru(self, file_path, upload_url):
        with open(file_path, "rb") as f:
            response = requests.put(upload_url, data=f)

        if response.status_code != 200:
            raise RuntimeError("Upload to MinerU failed")

        return True

    def get_task_result(self, batch_id: str):
        url = MINERU_TASK_RESULT_URL.format(batch_id=batch_id)
        headers = {
            "Authorization": self.auth_token,
            "Content-Type": "application/json",
        }

        response = requests.get(url, headers=headers)
        result = response.json()

        if result.get("code") != 0:
            raise RuntimeError(f"Get task result failed: {result.get('msg')}")

        return result