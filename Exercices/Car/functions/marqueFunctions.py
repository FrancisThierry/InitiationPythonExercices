def extract_unique_brands(car_models):
    """
    Extract unique car brands from a list of car models.

    Args:
        car_models (list): List of car model strings (e.g., "Ford BMax").

    Returns:
        tuple: A tuple of unique car brands.
    """
    brands = set()
    for model in car_models:
        # Ensure the model is a string before processing
        if isinstance(model, str):
            # Split the model string and take the first part as the brand
            brand = model.split()[0]
            brands.add(brand)
    return tuple(brands)
