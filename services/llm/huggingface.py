"""
Traven Hugging Face LLM.

Implementation of the BaseLLM interface using
Hugging Face Transformers.
"""

from transformers import pipeline

from services.llm.base import BaseLLM


class HuggingFaceLLM(BaseLLM):
    """
    Hugging Face implementation of BaseLLM.
    """

    def __init__(
        self,
        model_name: str,
        device: str = "cpu",
    ):
        """
        Parameters
        ----------
        model_name:
            Hugging Face model ID.

        device:
            "cpu", "cuda", or "auto".
        """

        self.model_name = model_name

        self.pipeline = pipeline(

            task="text-generation",

            model=model_name,

            device=device,

        )

    def generate(
        self,
        prompt: str,
        max_tokens: int = 300,
        temperature: float = 0.3,
    ) -> str:
        """
        Generate text from the model.
        """

        response = self.pipeline(

            prompt,

            max_new_tokens=max_tokens,

            temperature=temperature,

            do_sample=temperature > 0,

            return_full_text=False,

        )

        return response[0]["generated_text"].strip()
