import base64
import requests
import io
import os
from typing import Dict, List, Tuple

import gradio as gr
from PIL import Image

PORT = 9001
ADDRESS = "http://localhost"
ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY")


def encode_base64_pillow(image: Image) -> str:
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)
    encoded_image = base64.b64encode(buffer.read())
    return encoded_image.decode("ascii")


def compose_payload(image: Image, prompt: str, api_key: str) -> Dict:
    return {
        "image": {
            "type": "base64",
            "value": encode_base64_pillow(image),
        },
        "api_key": api_key,
        "prompt": prompt,
    }


image_component = gr.Image(type="pil", scale=1, height=400)
chatbot_component = gr.Chatbot(
    bubble_full_width=False,
    scale=2,
    height=400
)
text_prompt_component = gr.Textbox(label="Text Prompt", scale=7)
submit_button_component = gr.Button(value="Submit", scale=1)


def on_submit(
    image: Image, text_prompt: str, chatbot: List[Tuple[str, str]]
) -> Tuple[str, List[Tuple[str, str]]]:
    payload = compose_payload(image, text_prompt, ROBOFLOW_API_KEY)
    results = requests.post(
        f"{ADDRESS}:{PORT}/llm/cogvlm",
        json=payload,
    )
    response = results.json()["response"]
    chatbot.append((text_prompt, response))
    return "", chatbot


with gr.Blocks() as demo:
    with gr.Row():
        image_component.render()
        chatbot_component.render()
    text_prompt_component.render()
    submit_button_component.render()

    submit_button_component.click(
        fn=on_submit,
        inputs=[image_component, text_prompt_component],
        outputs=[text_prompt_component, chatbot_component],
        queue=False
    )
    text_prompt_component.submit(
        fn=on_submit,
        inputs=[image_component, text_prompt_component],
        outputs=[text_prompt_component, chatbot_component],
        queue=False
    )

demo.queue(max_size=99).launch(debug=False, show_error=True, share=True)
