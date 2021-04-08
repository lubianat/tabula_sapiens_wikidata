#!usr/bin/python3
import sys
import scanpy as sc
import pandas as pd

adata = sc.read(sys.argv[1])
name = sys.argv[2]

metadata = adata.obs
metadata.to_csv("annotations/"+name+"_tabula_sapiens_metadata_raw.csv")