import argparse
import base64
import os
from typing import Dict

import requests


def encode_base64(image_path: str) -> str:
    with open(image_path, "rb") as image:
        encoded_image = base64.b64encode(image.read())
    return encoded_image.decode("ascii")


def compose_payload(image_path: str, prompt: str, api_key: str) -> Dict:
    return {
        "image": {
            "type": "base64",
            "value": encode_base64(image_path),
        },
        "api_key": api_key,
        "prompt": prompt,
    }


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Send an image and a prompt to CogVLM inference server via API.")
    parser.add_argument(
        "--image",
        required=True,
        help="Specifies the path to the image file that will be sent to the inference "
             "server."
    )
    parser.add_argument(
        "--prompt",
        required=True,
        help="The prompt text that accompanies the image in the request to the CogVLM "
             "model."
    )
    parser.add_argument(
        "--port",
        type=int,
        default=9001,
        help="Optional. The port number of the API."
    )
    parser.add_argument(
        "--address",
        default="http://localhost",
        help="Optional. The address of the API."
    )
    parser.add_argument(
        "--api_key",
        help="Optional. The Roboflow API Key for authentication with the API. If not "
             "provided, the script looks for the 'ROBOFLOW_API_KEY' environment "
             "variable."
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    api_key = args.api_key or os.getenv("ROBOFLOW_API_KEY")
    if not api_key:
        raise ValueError(
            "API key is required. Pass as an argument or set the ROBOFLOW_API_KEY "
            "environment variable."
        )

    infer_payload = compose_payload(args.image, args.prompt, api_key)

    results = requests.post(
        f"{args.address}:{args.port}/llm/cogvlm",
        json=infer_payload,
    )
    print(results.json()["response"])
