from graph import create_ad_graph
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    graph = create_ad_graph()
    input_data = {
        "product_idea": "A car with solar panels",
        "ad_style": "Futuristic tech showcase",
        "num_images": 3,
        "image_style": "vivid", # "natural" for more realistic images, "vivid" for more artistic
        "image_quality": "standard" # "standard" for lower quality, "hd" for higher quality
    }
    result = graph.invoke(input_data)
    for i, image in enumerate(result["ad_images"], 1):
        print(f"Image {i}: {image['url']}")