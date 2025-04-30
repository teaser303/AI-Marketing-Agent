def input_node(state):
    """
    Input node to receive user input for product idea, ad style, and number of images.
    """
    # In a real application, this would be replaced with actual input handling
    # For now, we simulate it with a dictionary
    return {
        "product_idea": state.get("product_idea"),
        "ad_style": state.get("ad_style"),
        "num_images": state.get("num_images")
    }