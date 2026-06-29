import anndata as ad
from pathlib import Path


def read_file(path: str):
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found at {file_path}")
    
    if file_path.suffix != ".h5ad":
        raise ValueError(f"File format is not .h5ad, instead we've got: {file_path.suffix}")
    
    try:
        return ad.read_h5ad(file_path)
    except Exception as exc:
        raise ValueError(f"Could not read .h5ad file: {file_path}") from exc