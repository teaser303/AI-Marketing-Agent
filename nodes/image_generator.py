from openai import OpenAI
import time
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

def generate_images(state):
    prompts = state["image_prompts"]
    style = state["image_style"]
    quality = state["image_quality"]
    size = "1024x1024"
    image_results = []

    for prompt in prompts:
        try:
            print(f"Generating image for prompt: {prompt}")
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                n=1,
                size=size,
                quality=quality,  
                style=style
            )
            image_url = response.data[0].url
            image_results.append({
                "prompt": prompt,
                "url": image_url
            })

            time.sleep(1)  # Avoid rate limit

        except Exception as e:
            print(f"Failed to generate image: {e}")
            image_results.append({
                "prompt": prompt,
                "url": None,
                "error": str(e)
            })

    return {**state, "ad_images": image_results}