def output_node(state):
    return {
        "ad_images": state["ad_images"],
        "prompts_used": state["image_prompts"]
    }