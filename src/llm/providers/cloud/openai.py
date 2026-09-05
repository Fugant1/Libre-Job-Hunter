from llm.llm_base import LLMBase

class OpenAILLM(LLMBase):
    def __init__(self):
        super().__init__()

    def create_llm(self, model_name: str, **kwargs) -> Any:
        return

    def generate_response(self, prompt: str, **kwargs) -> str:
        return

    def batch_generate_responses(self, prompts: list[str], **kwargs) -> list[str]:
        return []