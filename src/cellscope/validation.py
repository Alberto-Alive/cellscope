from anndata import AnnData

def validate_adata(adata: AnnData):
    warnings = []
    errors = []

    if adata.n_obs < 1:
        errors.append(f"The dataset must have at least one cell/row: {adata.n_obs}")
    
    if adata.n_vars < 1:
        errors.append(f"The dataset must contain at least one gene/column: {adata.n_vars}")

    if not adata.var_names.is_unique:
        duplicate_genes = adata.var_names[adata.var_names.duplicated()].unique().tolist()
        warnings.append(f"Gene names are not unique: {duplicate_genes}")
    
    if not adata.obs_names.is_unique:
        duplicate_cells = adata.obs_names[adata.obs_names.duplicated()].unique().tolist()
        warnings.append(f"Cell names are not unique {duplicate_cells}")

    if adata.X is None:
        errors.append(f"Dataset is missing an expression matrix: {adata.X}")

    useful_obs_columns = ["batch", "sample", "condition"]

    missing_useful_columns = [col for col in useful_obs_columns if col not in adata.obs.columns]

    if missing_useful_columns:
        warnings.append(f"Missing useful columns {missing_useful_columns}")

    summary = {
        "n_cells": adata.n_obs,
        "n_genes": adata.n_vars,
        "is_valid": len(errors) == 0,
        "n_errors": len(errors),
        "n_warnings": len(warnings),
        "errors": errors,
        "warnings": warnings
    }

    return {
        "is_valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "summary": summary
    }