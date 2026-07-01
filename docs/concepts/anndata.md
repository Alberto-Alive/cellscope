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
