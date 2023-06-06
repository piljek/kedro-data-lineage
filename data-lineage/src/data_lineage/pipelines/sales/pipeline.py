"""
This is a boilerplate pipeline 'sales'
generated using Kedro 0.18.9
"""
import pandas as pd

from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    pipeline = Pipeline([
        node(
            list_columns,
            inputs=dict(
                    Sales = "Sales", # Sales data,
                    # Sales Columns:
                    Sales_OrderID= "params:Sales_OrderID",
                    Sales_CustomerID= "params:Sales_CustomerID",
                    Sales_ProductID= "params:Sales_ProductID" ,
                    Sales_Quantity= "params:Sales_Quantity",
                    Sales_SalesDate= "params:Sales_SalesDate",
                        ),
            outputs="Sales_Columns",
            tags=["sales_cols"]
        ),
        # node(
        # read_sales_dict
        # , inputs=dict( sales="params:Sales", OrderID= "params:Sales.OrderID", Test = "params:OrderID")
        # , outputs="sout"
        # ),
        # node(
        # func= lambda x: x,
        # inputs= ["parameters:Sales.OrderID"],
        # outputs="lambda_x",
        # name="LambdaReadingSalesData",
        # tags=["pri_tag"]
        # ),
        # node(func= read_sales_data,
        #         inputs= ["parameters:Sales.OrderID", "parameters:Sales"],
        #         outputs="sales_data",
        #         name="ReadingSalesData"
        #         ),
        # node(func= read_sales_data,
        #         inputs= ["sales_products_stock_flow", "parameters:Sales"],
        #         outputs="sales_sql_data",
        #         name="ReadingSalesSQL"
        #         ),
    ])
    return pipeline

def list_columns(**any):
    return

def read_sales_data(*kwargs):
    return
def read_sales_dict(**kwargs):
    return

def create_sales_SQL(df: pd.DataFrame):

    return
