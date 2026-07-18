"""
LLM Factory.

Creates and configures the language model used by Traven.

Responsibilities
----------------
✓ Instantiate the configured LLM
✓ Hide implementation details
✓ Provide a single entry point for model loading
"""

from services.llm.huggingface import HuggingFaceLLM


# ==========================================================
# Default Model
# ==========================================================

DEFAULT_MODEL = "Qwen/Qwen2.5-3B-Instruct"


# ==========================================================
# Factory
# ==========================================================

def create_llm(
    model_name: str | None = None,
    device: str = "cpu",
):
    """
    Create an LLM instance.

    Parameters
    ----------
    model_name:
        Hugging Face model name.

    device:
        cpu, cuda or auto.
    """

    return HuggingFaceLLM(

        model_name=model_name or DEFAULT_MODEL,

        device=device,

    )
