"""LLM setup for the insight agent."""

from __future__ import annotations

import logging
import os
from pathlib import Path

from langchain_groq import ChatGroq

logger = logging.getLogger(__name__)


def _load_env_file() -> None:
    """Load key-value pairs from a local .env file if it exists."""

    env_path = Path(__file__).resolve().parent.parent / ".env"
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        stripped_line = line.strip()
        if not stripped_line or stripped_line.startswith("#") or "=" not in stripped_line:
            continue

        key, value = stripped_line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


_load_env_file()


def get_llm() -> ChatGroq:
    """Return the Groq chat model used for insights."""

    model_name = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
    if not os.getenv("GROQ_API_KEY"):
        logger.warning("GROQ_API_KEY is not set. Insight generation will fall back to a local summary.")
    return ChatGroq(model=model_name, temperature=0.2)
