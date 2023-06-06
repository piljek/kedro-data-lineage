from sales_pipeline.sales_node import SalesNodes
from kedro.pipeline import Pipeline
from kedro.pipeline import node
import pandas as pd
# from data_lineage.pipelines.sales_pipeline.sales_node import SalesNodes


def create_pipeline(**kwargs) -> Pipeline:
    pipeline = Pipeline([
        node(func= read_sales_data,
                inputs= ["parameters:Sales.OrderID", "parameters:Sales"],
                outputs="sales_data",
                name="ReadingSalesData"
                ),
        node(func= read_sales_data,
                inputs= ["sales_products_stock_flow", "parameters:Sales"],
                outputs="sales_sql_data",
                name="ReadingSalesSQL"
                ),
    ])
    return pipeline

def read_sales_data(*kwargs):
    return

def create_sales_SQL(df: pd.DataFrame):
    
    return