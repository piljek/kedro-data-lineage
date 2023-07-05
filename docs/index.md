# kedro-data-lineage

This GitHub repository provides a comprehensive demonstration of a data lineage implementation using Kedro, an open-source Python library, and various source systems. This repository showcases the setup and utilization of pipelines described in the Medium Blog Post to demonstrate enablement of data lineage.

**Data lineage** refers to the process of documenting and tracking the journey of data from its origin to its final destinations, encompassing the various systems and transformations it undergoes along the way.

Through interactive exploration and visualization, the repository illustrates the modeling of projections across source systems, calculation of key performance indicators (KPIs), and derivation of sales statistics. The code and examples provided offer valuable insights into establishing data lineage, ensuring data quality, and facilitating impact analysis in enterprise data pipelines.


## Repository Setup

This repository is set up using Poetry, a dependency management tool for Python. It provides a streamlined environment for managing project dependencies. To ensure a consistent and reproducible development environment, we recommend installing Miniconda, a lightweight distribution of Conda, before setting up the project locally. With Poetry and the local environment in place, you can easily manage dependencies and explore the power of data lineage using Kedro. Refer to the documentation for detailed instructions on setting up the environment and utilizing the repository for data lineage analysis.
```bash
# Creates local python environment
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
# --> enter human readable project name: 
data_lineage
```
## Build project
To build the project, follow these steps:

1. Clone the repository using the following command:
    ```
    git clone <repository-url>
    ```

2. Create a local environment by navigating to the project directory and executing the command:
    ```
    $ conda create -p ./env python=3.8
    $ conda activate
    ```

3. Activate the local environment. The command may vary depending on your operating system:
   - For Windows:
   ```
   $ env\Scripts\activate
   ```
   - For macOS/Linux:
   ```
   $ conda activate ./env
   ```

4. Install the project dependencies using Poetry. Run the following command:
    ```
    $ poetry install -vvv
    ```

With these steps completed, the project will be set up, and the necessary dependencies will be installed in the local environment. You can now proceed with building and running the project using the provided scripts and commands.

## Kedro

### Kedro Viz
Navigate to the source directory and start the React component
````
$ cd data-lineage
$ kedro viz
````
### Kedro pipeline creation
Create new pipeline that is automatically registered
```bash
$ kedro pipeline create <enter name>
```
This will create the `<enter name>` package and creates `__init__.py, pipeline.py` and `node.py` classes. The pipeline class already contains a method stub for a pipeline as starting point. 

