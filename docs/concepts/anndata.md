# AnnData and `.h5ad`

## What problem this solves

Is a way to store biological data as an object containing cell metadata, gene metadata, embeddings, annotations, analysis outputs, and expression matrices.


## Core object

```text
cells x genes
```

## Key fields

```text
adata.X         main expression matrix
adata.obs       cell metadata
adata.var       gene metadata
adata.layers    alternative amtrices
adata.obsm      embeddings like PCA, UMAP, scVI  -> obsm means observation matrices :))
adata.uns       unstructured analysis outputs
```


### `adata.X`

Important question lol

> Does `adata.X` contain raw counts, normalized values, or log-trasnformed values?

-> matters bcs different pipelines steps expect different forms of data.


### `adata.obs`

Cell metadata example:

```text
sampel_id
donor_id
batch
condition
cell_type
n_genes_by_counts
total_counts
pct_counts_mt
```

### `adata.var`

Gene metadata, for example:

```text
gene_symbol
gene_id
highly_variable
mt
```

### `adata.layers`

Alternative matrices:

```text
adata.layers["counts"]
adata.layers["normalized"]
```

### `adata.obsm`

Cell embeddings:

```text
adata.obsm["X_pca"]
adata.obsm["X_umap"]
adata.obsm["X_scVI"]
```


## What can go wrong?

... so much lol

- `adata.X` does not contain what you think it contains
- raw counts were overwritten
- cell IDs are duplciated
- gene IDs are duplicated
- batch or donor labels are wrong
- gene symbols and gene IDs are mixed up
- sparse matrices are accidentally converted to dense matrices
- embeddings are stale after filtering cells

