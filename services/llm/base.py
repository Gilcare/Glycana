"""
LLM Base Interface.

Defines the common interface for all supported
Large Language Models (LLMs).

Responsibilities
----------------
✓ Define a standard interface
✓ Ensure all providers behave consistently

This module does NOT:
---------------------
✗ Load models
✗ Call Hugging Face
✗ Call OpenAI
✗ Build prompts
"""

from abc import ABC
from abc import abstractmethod


class BaseLLM(ABC):
    """
    Abstract base class for all LLM providers.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str,
        max_tokens: int = 300,
        temperature: float = 0.3,
    ) -> str:
        """
        Generate a response from the language model.

        Parameters
        ----------
        prompt:
            Input prompt.

        max_tokens:
            Maximum number of new tokens.

        temperature:
            Sampling temperature.

        Returns
        -------
        str
            Generated text.
        """
        raise NotImplementedError
