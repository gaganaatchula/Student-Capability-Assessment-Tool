import openai
import os
from dotenv import load_dotenv
import re

load_dotenv()

def get_api_key(service_name):
    """Retrieve API key from environment variables based on service name."""
    env_var_name = f"{service_name.upper()}_API_KEY"
    api_key = os.getenv(env_var_name)

    if not api_key:
        raise ValueError(f"API key for {service_name} not found in environment variables.")

    return api_key

# formatting.py
def format_chat_history(chat_history, family):
    """Format chat history based on LLM family."""
    formatted_history = []
    if len(chat_history) > 0:
        for history in chat_history:
            user_content = history["user"]
            assistant_content = history["assistant"]
            if family == "gemini":
                formatted_history.extend([
                    {"role": "user", "parts": [user_content]},
                    {"role": "model", "parts": [assistant_content]}
                ])

            else:
                formatted_history.extend([
                    {"role": "user", "content": user_content},
                    {"role": "assistant", "content": assistant_content}
                ])
    return formatted_history

def handle_openai(context):
    """Handle requests for OpenAI models."""
    if not context["supports_image"] and context.get("image_urls"):
        return "Images are not supported by selected model."
    try:
        openai.api_key = get_api_key("openai")

        messages = format_chat_history(context["chat_history"], "openai") + [
            {"role": "system", "content": context["SYSTEM_PROMPT"]},
            {"role": "assistant", "content": context["phase_instructions"]},
            {"role": "user", "content": context["user_prompt"]}
        ]

        if context["supports_image"] and context["image_urls"]:
            messages.insert(2, {"role": "user", "content": [{"type": "image_url", "image_url": {"url": url}} for url in
                                                            context["image_urls"]]})

        response = openai.chat.completions.create(
            model=context["model"],
            messages=messages,
            temperature=context["temperature"],
            max_tokens=context["max_tokens"],
            top_p=context["top_p"],
            frequency_penalty=context["frequency_penalty"],
            presence_penalty=context["presence_penalty"]
        )

        input_price = int(response.usage.prompt_tokens) * context["price_input_token_1M"] / 1000000
        output_price = int(response.usage.completion_tokens) * context["price_output_token_1M"] / 1000000
        total_price = input_price + output_price
        context['TOTAL_PRICE'] += total_price

        return response.choices[0].message.content

    except Exception as e:
        return f"Unexpected error while handling OpenAI request: {e}"
HANDLERS={"openai":handle_openai}