import torch
from diffusers import DiffusionPipeline
import os
import runpod

# Load model on startup
print("Loading FLUX Schnell model...")
pipe = DiffusionPipeline.from_pretrained(
    "Hardik2410/flux-schnell-hf",  # Your uploaded HF model
    torch_dtype=torch.float16,
    variant="fp16"
).to("cuda")

def generate_image(job):
    prompt = job["input"].get("prompt", "a fantasy landscape")
    image = pipe(prompt).images[0]

    # Save to file or return raw image data
    image_path = f"/tmp/generated_{job['id']}.png"
    image.save(image_path)
    return {"image_path": image_path}

runpod.serverless.start({"handler": generate_image})
