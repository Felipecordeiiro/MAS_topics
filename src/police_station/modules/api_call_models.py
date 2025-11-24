from crewai import LLM

def _get_ollama_base_url() -> str:
    """
    Returns the appropriate Ollama base URL depending on the environment.
    """
    return "http://localhost:11434"


def _llm_default() -> LLM:
    return LLM(
        model="ollama/qwen2.5:latest",
        base_url=_get_ollama_base_url(),
        api_key="ollama",
        temperature=0.7,
        max_tokens=400,
    )

def _llm_leader() -> LLM:
    return LLM(
        model="ollama/llama3.2:latest",
        base_url=_get_ollama_base_url(),
        temperature=0.7,
        api_key="ollama",
        max_tokens=2048,
    )