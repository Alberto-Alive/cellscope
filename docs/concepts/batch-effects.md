# Batch effect

## What problem this solve

A batch effect is non-biological variation caused by how data was generated.

Data collection is always the root cause of many problems, the lack of specific workflows makes this a real problem. In single cell datasets this means that cell samples are collected from different donors, labs, protocols, sequencing, runs or dates - makign cells look different for technical reasons not bio.


## Failure example

Suppose:

- all healthy samples were processed in batch A
- all disease samples were processed in batch B

q: is it because disease or batch?