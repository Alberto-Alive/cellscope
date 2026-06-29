from anndata import AnnData

def validate_file(adata: AnnData):
    warnings = []

    if adata.n_obs < 1:
        raise ValueError(f"The file must have at least one cell/row: {adata.n_obs}")
    
    if adata.n_vars < 1:
        raise ValueError(f"The file must contain at least one gene/column: {adata.n_vars}")

    if not adata.var_names.is_unique:
        duplicate_genes = adata.var_names[adata.var_names.duplicated()].unique().tolist()
        warnings.append(f"Gene names are not unique: {duplicate_genes}")
    
    if not adata.obs_names.is_unique:
        duplicate_cells = adata.obs_names[adata.obs_names.duplicated()].unique().tolist()
        warnings.append("Cell names are not unique")

    if adata.X is None:
