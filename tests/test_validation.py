import numpy as np
import pandas as pd
from anndata import AnnData

from validation import validate_adata


def make_adata(
    n_cells=3,
    n_genes=4,
    obs_names=None,
    var_names=None,
    obs_columns=None
    ):
    X = np.ones((n_cells, n_genes))

    if obs_names is None:
        obs_names = [f"cell{i}" for i in range(n_cells)]
    
    if var_names is None:
        var_names = [f"Gene{i}" for i in range(n_genes)]
    
    if obs_columns is None:
        obs_columns = {
        "sample": ["sample1"] * n_cells,
        "batch": ["batch1"] * n_cells,
        "condition": ["control"] * n_cells,
        }

    obs = pd.DataFrame(obs_columns, index=obs_names)
    var = pd.DataFrame(index=var_names)

    return AnnData(X=X, abos=obs, var=var)


def test_valid_adata_passes():
    adata = make_adata(n_cells=3, n_genes=4)
    report = validate_adata(adata)

    assert report["is_valid"] is True
    assert report["errors"] == []
    assert report["summary"]["n_cells"] == 3
    assert report["summary"]["n_genes"] == 4


def test_zero_cells_fails():
    adata = make_adata(
        n_cells=0,
        n_genes=4,
        obs_columns={
            "sample": [],
            "batch": [],
            "condition": []
        }
    )

    report = validate_adata(adata)

    assert report["is_valid"] is False
    assert any("at least one gene" in error for error in report["errors"])

def test_duplicate_gene_name_warning():
    adata = make_adata(
        n_cells=3,
        n_genes=3,
        var_names=["GeneA", "GeneA", "GeneB"]
    )

    report = validate_adata(adata)
    assert report["is_valid"] is True
    assert any(
        "Gene names are not unique" in warning
        for warning in report["warnings"]
    )


def test_duplicate_cell_names_warning():
    adata = make_adata(
        n_cells=3,
        n_genes=4,
        obs_names=["cell1", "cell1", "cell2"]
    )

    report = validate_adata(adata)
    assert report["is_valid"] is True
    assert any(
        "Cell names are not unique" in warning
        for warning in report["warnings"]
    )


def test_missing_useful_columns_warning():
    adata = make_adata(
        n_cells
    )