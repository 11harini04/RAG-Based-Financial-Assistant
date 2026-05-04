def validate_response(response):
    # Prevent hallucination
    if "I don't have enough data" in response:
        return response

    # Basic financial safety
    risky_terms = ["guaranteed returns", "no risk"]
    for term in risky_terms:
        if term in response.lower():
            return "Potentially unsafe financial advice detected."

    return response