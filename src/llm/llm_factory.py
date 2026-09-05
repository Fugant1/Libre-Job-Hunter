from llm.llm_base import LLMBase
from src.llm.providers.cloud.openai import OpenAILLM
#from llm.cloud.anthropic import AnthropicLLM
#from llm.cloud.ollama import OllamaLLM

providers = {
    "openai": OpenAILLM,
#    "anthropic": AnthropicLLM,
#    "ollama": OllamaLLM,
}

def get_llm_provider(provider_name: str) -> LLMBase:
    provider_class = providers.get(provider_name.lower())
    if provider_class is None:
        raise ValueError(f"Unsupported LLM provider: {provider_name}")
    return provider_class()