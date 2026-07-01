# Cell type annotations
 

 # What problem this solves


 Cell type annotations assigns biological labels to cells or clusters.

 Ex:


 ```text
 cluster 0 -> CD4 T cells
 cluster 1 -> B cells
 cluster 2 -> monocytes
 cluster 3 -> NK cells
 ```

 ## Basic workflow

 ```text
cluster cells
find marker genes per cluster
compare markers against known biology
assign labels
validate labels across samples/batches
flag uncertain clusters
```


## Marker genes

```text
long list... basically each cell type has a prominent rna expression
```

## Some bio important distinction

Cell type is not the same as cell state.. of course.