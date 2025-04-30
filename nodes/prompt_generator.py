from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

def generate_prompts(state):
    system_prompt = "You're a creative advertising prompt writer for AI image generators."

    user_input = (
        f"Product idea: {state['product_idea']}\n"
        f"Ad style: {state['ad_style']}\n"
        f"Generate {state['num_images']} highly visual prompts for this product idea "
        f"in the given advertising style. Make each prompt distinct and image-ready."
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    prompts = response.choices[0].message.content.strip().split("\n")

    return {**state, "image_prompts": [p for p in prompts if p.strip()]}