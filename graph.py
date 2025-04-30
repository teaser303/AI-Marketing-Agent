from langgraph.graph import StateGraph
from typing import TypedDict, Literal
from nodes.input import input_node
from nodes.prompt_generator import generate_prompts
from nodes.image_generator import generate_images
from nodes.output import output_node


class State(TypedDict):
    product_idea: str
    ad_style: str
    num_images: int
    image_style: Literal['vivid', 'natural']
    image_quality: Literal['standard', 'hd', 'low', 'medium', 'high', 'auto']
    image_prompts: list[str]
    ad_images: list[dict]
    

def create_ad_graph():
    builder = StateGraph(State)
    
    builder.add_node("input", input_node)
    builder.add_node("prompt", generate_prompts)
    builder.add_node("image", generate_images)
    builder.add_node("output", output_node)

    builder.set_entry_point("input")
    builder.add_edge("input", "prompt")
    builder.add_edge("prompt", "image")
    builder.add_edge("image", "output")

    return builder.compile()