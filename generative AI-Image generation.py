from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to("cuda")  # or "cpu" if no GPU

prompt = "A futuristic cityscape at sunset"
image = pipe(prompt).images[0]

image.show()