# kedro-data-lineage

# Setup

```bash
$ conda create -p ./env python=3.8
$ conda activate

# Create poetry if not existent
$ poetry init
$ poetry install -vvv

# Install Kedro using conda
$ conda install -c conda-forge kedro
# Test installation
$ kedro info

# Kedro Viz
$ poetry add kedro-viz

# Pyarrow for parquet files
$ poetry add kedro pandas pyarrow 

# SQL Files
$ poetry add SQLAlchemy psycog2
```

Setup new Kedro Project
```bash
$ kedro new
--> enter humand readable project name: 
data_lineage
```

Create new pipeline that is automatically registered
```bash
$ kedro pipeline create <enter name>
```
This will create the `<enter name>` package and creates `__init__.py, pipeline.py` and `node.py` classes. The pipeline class already contains a method stub for a pipeline as starting point. 