class HuggingFaceLLM:

    def __init__(self, pipeline):
        self.pipeline = pipeline

    def generate(self, prompt: str) -> str:

        response = self.pipeline(
            prompt,
            max_new_tokens=300,
            do_sample=False,
        )

        return response[0]["generated_text"]
