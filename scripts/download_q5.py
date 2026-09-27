import os
from huggingface_hub import hf_hub_download

repo_id = "LiquidAI/LFM2.5-2.6B-GGUF"
models_dir = r"c:\Yash\edge-llm-benchmarks\models"
os.makedirs(models_dir, exist_ok=True)

file = "LFM2.5-2.6B-Q5_K_M.gguf"
print(f"Downloading {file}...")
hf_hub_download(
    repo_id=repo_id,
    filename=file,
    local_dir=models_dir,
    local_dir_use_symlinks=False
)
print(f"Finished downloading {file}.")
