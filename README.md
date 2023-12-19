# cog-vlm-client

## 👋 hello

This script is designed to send an image and a prompt to 
[inference](https://github.com/roboflow/inference) server running the 
[CogVLM](https://github.com/THUDM/CogVLM) model.

## 💻 install

- clone repository and navigate to root directory

    ```bash
    git clone https://github.com/roboflow/cog-vlm-client.git
    cd cog-vlm-client
    ```
  
- setup python environment and activate it [optional]

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
  
- install required dependencies

    ```bash
    pip install -r requirements.txt
    ```

## 🛠️ script arguments

- `--image`: Specifies the path to the image file that will be sent to the inference 
server.
- `--prompt`: The prompt text that accompanies the image in the request to the CogVLM 
model.
- `--port` (optional): The port number of the API. Defaults to `9001` if not specified.
- `--address` (optional): The address of the API. Defaults to `http://localhost` if not
specified.
- `--api_key` (optional): The Roboflow API key used for authentication with the API. If 
not provided, the script will look for the `ROBOFLOW_API_KEY` environment variable.
