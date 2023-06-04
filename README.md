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
```

Setup new Kedro Project
```bash
$ kedro new
--> enter humand readable project name: 
data_lineage

```