This is a follow up project on exploring how a biological workflow service would work end to end.


The platform would intake a .h5ad single-cell dataset, validate it, run a QC/preprocessing step then a simple "cell type prediction" step, store the results. It will expose both CLI and API access and will have some tests.





The goal is to familiarise with the biological workflow:

1. define the scientific question
2. set an input contract
3. validate the data
4. run the biological or model-processing steps
5. produce stable outputs
6. record provenance
7. test workflow on small known data

Preserving single-cell data:
- cell and gene metadata must be valid
- raw data should not be silently overwritten
- QC decisions should be recorded
- outputs should have stable schemas
- model.config/software versions should be tracked
- warnings should eb visible
- results should be reproducible


## Core workflow pattern

Every pipeline should answer the same questions:

```text
What scientific problem does this solve?
What input does it expect?
What assumptions does it make?
What validation happens before analysis?
What preprocessing steps happen?
What outputs are produced?
What provenance is recorded?
What can go wrong?
How do we test it?
```
