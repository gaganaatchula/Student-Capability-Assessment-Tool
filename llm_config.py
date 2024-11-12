# llm_config.py

LLM_CONFIG = {
    "gpt-4o-mini": {
        "family": "openai",
        "model": "gpt-4o-mini",
        "max_tokens": 1000,
        "temperature": 1.0,
        "top_p": 1.0,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "supports_image": False,
        "price_input_token_1M": 0.15,
        "price_output_token_1M": 0.60
    },
    "gpt-4-turbo": {
        "family": "openai",
        "model": "gpt-4-turbo",
        "max_tokens": 1000,
        "temperature": 1.0,
        "top_p": 1.0,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "supports_image": True,
        "price_input_token_1M": 10,
        "price_output_token_1M": 30
    },
    "gpt-4o": {
        "family": "openai",
        "model": "gpt-4o",
        "max_tokens": 250,
        "temperature": 0.0,
        "top_p": 1.0,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "supports_image": False,
        "price_input_token_1M": 5,
        "price_output_token_1M": 15
    }
}
