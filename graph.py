from langgraph.graph import StateGraph
from typing import TypedDict, Literal
from nodes.prompt_generator import generate_prompts
from nodes.image_generator import generate_images

class State(TypedDict):
    product_idea: str
    ad_style: str
    num_images: int
    image_style: Literal['vivid', 'natural']
    image_quality: Literal['standard', 'hd']
    image_prompts: list[str]
    ad_images: list[dict]
    

def create_ad_graph():
    builder = StateGraph(State)
    
    builder.add_node("prompt", generate_prompts)
    builder.add_node("image", generate_images)

    builder.set_entry_point("prompt")
    builder.add_edge("prompt", "image")

    return builder.compile()