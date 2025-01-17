# In this file, we define download_model
# It runs during container build time to get model weights built into the container

# In this example: A Huggingface BERT model

# from transformers import pipeline
import gdown
from pathlib import Path
from contextlib import redirect_stdout

import sys
import hashlib
import os



def download_model():
    # # do a dry run of loading the huggingface model, which will download weights
    # # pipeline('fill-mask', model='bert-base-uncased')
    print("hello world from download_model() in download.py")

    model_name="u2net"

    # md5 = "60024c5c889badc19c04ad937298a77b"
    # url = "https://drive.google.com/uc?id=1tCU5MM1LhRgGou5OpmpjBQbSrYIUoYab"


    from urllib import request


    home = os.getenv("U2NET_HOME", os.path.join("~", ".u2net"))
    path = Path(home).expanduser() / f"{model_name}.onnx"
    path.parents[0].mkdir(parents=True, exist_ok=True)


    

    if not path.exists():
        print(f"Downloading u2net.onnx to {path}")
        url = "https://u2net-model-weights.s3.ap-southeast-2.amazonaws.com/u2net.onnx"
        local_file = 'u2net.onnx'
        request.urlretrieve(url, local_file)
        # with redirect_stdout(sys.stderr):
        #     gdown.download(url, str(path), use_cookies=False)
    else:
        print(f"Found file: {model_name}.onnx at path: {path}")
    #     hashing = hashlib.new("md5", path.read_bytes(), usedforsecurity=False)
    #     if hashing.hexdigest() != md5:
    #         with redirect_stdout(sys.stderr):
    #             gdown.download(url, str(path), use_cookies=False)

    
if __name__ == "__main__":
    download_model()
    print("hello world from __main__ in download.py")