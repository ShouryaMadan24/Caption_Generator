from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

def generate_captions(description, num_return_sequences=3):
    prompt = f"Instagram post: {description}\nCaption:"
    outputs = generator(prompt, max_length=60, num_return_sequences=num_return_sequences, temperature=0.9)
    return [output['generated_text'].replace(prompt, '').strip() for output in outputs]