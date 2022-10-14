from transformers import pipeline
import torch
import rembg
from PIL import Image
import requests
from io import BytesIO
import base64

# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    global model
    
    # device = 0 if torch.cuda.is_available() else -1
    # model = pipeline('fill-mask', model='bert-base-uncased', device=device)

# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs:dict) -> dict:
    global model

    # Parse out your arguments
    url = model_inputs.get('url', None)
    if url == None:
        return {'message': "No url provided"}
    
    # Run the model
    # result = model(prompt)



    # url="https://images.pexels.com/photos/207582/pexels-photo-207582.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))


    result = rembg.remove(img)

    ## Save the new image as a b64 enconded string
    buffered = BytesIO()
    result.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue())
    
    
    # Return the bytes
    # return str(img_str)
    return(str(img_str))
    # return 'hello'
