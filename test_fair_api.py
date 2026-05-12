import requests
import json
import time
from pathlib import Path

# =========================================================
# FAIR MOCK API CLIENT
# MARSAIL — Motor AI Recognition Solution Laboratory
# Developer: Teerapong Panboonyuen (Kao)
# =========================================================

API_URL = "http://localhost:8000/fair/analyze"

IMAGE_PATH = "sample_image/TESLA_TOY.png"

HEADERS = {
    "accept": "application/json"
}


def print_banner():
    print("\n" + "=" * 70)
    print("FAIR — Filter And Image Removal")
    print("MARSAIL — Motor AI Recognition Solution AI Laboratory")
    print("=" * 70 + "\n")


def validate_image_exists(image_path):
    if not Path(image_path).exists():
        raise FileNotFoundError(
            f"[ERROR] Image not found: {image_path}"
        )


def send_request(image_path):

    validate_image_exists(image_path)

    with open(image_path, "rb") as image_file:

        files = {
            "file": image_file
        }

        print("[INFO] Sending image to FAIR API...")
        start = time.time()

        response = requests.post(
            API_URL,
            headers=HEADERS,
            files=files
        )

        latency = time.time() - start

    print(f"[INFO] Response received in {latency:.3f}s\n")

    return response


def pretty_print_response(response):

    print("=" * 70)
    print(f"HTTP STATUS: {response.status_code}")
    print("=" * 70)

    try:

        data = response.json()

        print(
            json.dumps(
                data,
                indent=2,
                ensure_ascii=False
            )
        )

    except Exception:

        print("[ERROR] Invalid JSON response")
        print(response.text)


if __name__ == "__main__":

    print_banner()

    response = send_request(IMAGE_PATH)

    pretty_print_response(response)