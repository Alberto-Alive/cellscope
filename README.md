This is a follow up project on exploring how a biological workflow service would work end to end.


The platform would intake a .h5ad single-cell dataset, validate it, run a QC/preprocessing step then a simple "cell type prediction" step, store the results. It will expose both CLI and API access and will have some tests.