import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

# --- Directory Configuration ---
MARKDOWN_DIR = BASE_DIR / "markdown_docs"
PARENT_STORE_PATH = BASE_DIR / "parent_store"
QDRANT_DB_PATH = BASE_DIR / "qdrant_db"

# --- Qdrant Configuration ---
CHILD_COLLECTION = "document_child_chunks"
SPARSE_VECTOR_NAME = "sparse"

# --- Load Secrets from JSON (if exists) ---
SECRETS_FILE = Path(__file__).parent / "config_secrets.json"
_secrets = {}
if SECRETS_FILE.exists():
    try:
        with open(SECRETS_FILE, 'r', encoding='utf-8') as f:
            _secrets = json.load(f)
    except Exception as e:
        print(f"Warning: Could not load secrets file: {e}")

# --- Model Configuration ---
DENSE_MODEL = "BAAI/bge-base-zh-v1.5"
DENSE_MODEL_KWARGS = {"device": "cpu"}
DENSE_ENCODE_KWARGS = {"normalize_embeddings": True}
SPARSE_MODEL = "Qdrant/bm25"

DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY") or _secrets.get("DASHSCOPE_API_KEY", "")
DASHSCOPE_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
LLM_PROVIDER = "dashscope"
LLM_MODEL = "qwen-max"
LLM_TEMPERATURE = 0
# LLM_MODEL = "qwen3:4b-instruct-2507-q4_K_M"
# LLM_TEMPERATURE = 0

# --- Text Splitter Configuration ---
CHILD_CHUNK_SIZE = 500
CHILD_CHUNK_OVERLAP = 100
MIN_PARENT_SIZE = 2000
MAX_PARENT_SIZE = 10000
HEADERS_TO_SPLIT_ON = [
    ("#", "H1"),
    ("##", "H2"),
    ("###", "H3")
]
