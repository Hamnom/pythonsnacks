from transformers import pipeline
import torch
#pip install torch
#pip install transformers
generator = pipeline('text-generation', model='openai-community/gpt2', torch_dtype=torch.float16, device=0)

prompt = "Can you write me FAQs for Masters in data science enrollement in USA?"
result = generator(prompt, max_new_tokens=400, num_return_sequences=1)

print(result[0]['generated_text'])