import anndata as ad
from pathlib import Path


def read_file(path: str):
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found at {file_path}")
    
    if file_path.suffix != ".h5ad":
        raise ValueError(f"File format is not .h5ad, instead we've got: {file_path.suffix}")