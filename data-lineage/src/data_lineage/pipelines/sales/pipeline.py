"""
This is a boilerplate pipeline 'sales'
generated using Kedro 0.18.9
"""
import pandas as pd

from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    sales_pipeline = pipeline([
        node(
            list_columns,
            inputs=dict(
                    Sales = "Sales_", # Sales data,
                    # Sales Columns:
                    Sales_OrderID= "params:Sales_OrderID",
                    Sales_CustomerID= "params:Sales_CustomerID",
                    Sales_ProductID= "params:Sales_ProductID" ,
                    Sales_Quantity= "params:Sales_Quantity",
                    Sales_SalesDate= "params:Sales_SalesDate",
                    Sales_SalesValue = "params:Sales_SalesValue"
                        ),
            outputs="Sales",
            tags=["sales"]
        ),

    ], namespace = "Sales")
    return sales_pipeline

def list_columns(**any):
    return

def read_sales_data(*kwargs):
    return
def read_sales_dict(**kwargs):
    return

def create_sales_SQL(df: pd.DataFrame):

    return
