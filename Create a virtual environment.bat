:: Create a virtual environment
python -m venv .venv
.venv\Scripts\activate

:: Upgrade pip and install dependencies
python.exe -m pip install --upgrade pip
pip install -r requirements.txt

:: Install additional packages
pip install pytest
pip uninstall torch torchvision torchaudio -y
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install ultralytics
pip install --upgrade fastapi pydantic gradio starlette
pip install lapx
pip install openvino
pip install onnx onnxruntime

:: Install NVIDIA TensorRT
pip install --upgrade pip setuptools wheel
pip install nvidia-pyindex
pip install nvidia-tensorrt

:: Install CLIP
pip install git+https://github.com/openai/CLIP.git

:: Download the pre-trained model
Invoke-WebRequest -Uri "https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10n.pt" -OutFile "yolov10n.pt"

:: Prepare COCO dataset
python prepare_coco.py

:: Check the PyTorch environment
python -m torch.utils.collect_env
