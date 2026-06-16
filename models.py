# from dotenv import load_dotenv
# from openai import OpenAI
# import os
#
# load_dotenv()
#
# client=OpenAI(
#     base_url = "https://integrate.api.nvidia.com/v1",
#     api_key = os.getenv("NVIDIA_API_KEY")
# )
#
# MODELS = {
#     "Llama":
#     "meta/llama-3.3-70b-instruct",
#
#     "DeepSeek":
#     "deepseek-ai/deepseek-r1",
#
#     "Mixtral":
#     "mistralai/mixtral-8x7b-instruct-v0.1"
# }
#
# def ask_model(model,prompt):
#     response=client.chat.completions.create(
#         model=model,
#         messages=[{"role":"user","content":prompt}],
#         temperature=0.7,
#         max_tokens=500
#     )
#
#     return response.choices[0].message.content
#
# # from ai_arena.models import ask_model
#
# print(ask_model("Llama", "Hello, please introduce yourself in one sentence."))
# # Or use a raw model id:
# # print(ask_model("meta/llama-3.3-70b-instruct", "Hello..."))

# ai-arena/models.py
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

API_KEY = os.getenv("NVIDIA_API_KEY")
if not API_KEY:
    raise RuntimeError("Missing NVIDIA_API_KEY environment variable. Add it to your .env file or export it.")

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

# MODELS = {
#     "Llama": "meta/llama-3.3-70b-instruct",
#     "DeepSeek": "deepseek-ai/deepseek-r1",
#     "Mixtral": "mistralai/mixtral-8x7b-instruct-v0.1"
# }
MODELS = {
    "Llama 3.3 70B": "meta/llama-3.3-70b-instruct",
    "Mixtral 8x7B": "mistralai/mixtral-8x7b-instruct-v0.1",
    "Minimax M3": "minimaxai/minimax-m3",
    "Kimi K2.6": "moonshotai/kimi-k2.6"
}

def _extract_content(response):
    """Robustly extract assistant text from different response shapes."""
    try:
        # SDK object style
        return response.choices[0].message.content
    except Exception:
        pass
    try:
        # Dict-like style
        return response["choices"][0]["message"]["content"]
    except Exception:
        pass
    # fallback
    return str(response)


# def ask_model(model: str, prompt: str, temperature: float = 0.7, max_tokens: int = 500) -> str:
#     """
#     Ask the given model a prompt and return the assistant text.
#     'model' can be a friendly name from MODELS (e.g. "Llama") or a raw model id.
#     """
#     model_id = MODELS.get(model, model)  # map friendly name -> real id
#
#     try:
#         response = client.chat.completions.create(
#             model=model_id,
#             messages=[{"role": "user", "content": prompt}],
#             temperature=temperature,
#             max_tokens=max_tokens
#         )
#     except Exception as e:
#         # Detect likely 404 / NotFound case and show helpful text
#         msg = str(e)
#         if "404" in msg or "NotFound" in msg or "not found" in msg.lower():
#             raise RuntimeError(
#                 f"Model not found: '{model_id}'.\n"
#                 "Possible causes:\n"
#                 "- The model id is incorrect or not available to your account.\n"
#                 "- The provider (NVIDIA Integrate) does not host that model.\n"
#                 "Check your model id or try a model you know is available."
#             ) from e
#         raise  # re-raise other exceptions
#
#     return _extract_content(response)
#
def ask_model(model: str, prompt: str, temperature: float = 0.7, max_tokens: int = 500) -> str:
    """
    Ask the given model a prompt and return the assistant text.
    'model' can be a friendly name from MODELS (e.g. "Llama") or a raw model id.
    """
    model_id = MODELS.get(model, model)

    try:
        response = client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=130  # Add 30-second timeout
        )
    except Exception as e:
        msg = str(e)
        if "404" in msg or "NotFound" in msg or "not found" in msg.lower():
            raise RuntimeError(
                f"Model not found: '{model_id}'.\n"
                "Possible causes:\n"
                "- The model id is incorrect or not available to your account.\n"
                "- The provider (NVIDIA Integrate) does not host that model.\n"
                "Check your model id or try a model you know is available."
            ) from e
        raise

    return _extract_content(response)
# Example usage (commented for library usage):
# if __name__ == "__main__":

# print(ask_model("Llama","Hello, please introduce yourself in one sentence."))