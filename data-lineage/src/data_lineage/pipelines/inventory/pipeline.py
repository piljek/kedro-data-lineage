"""
This is a boilerplate pipeline 'products'
generated using Kedro 0.18.9
"""

from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    """A ``Pipeline`` defined as a collection of ``Node`` objects. This class
    treats nodes as part of a graph representation and provides inputs,
    outputs and execution order.
    """

    inventory_products_pipeline = pipeline([
        node(
            func=list_columns,
            inputs=dict(Products="Products_",
                        Products_ProductID="params:Products_ProductID",
                        Products_ProductName="params:Products_ProductName",
                        Products_Category="params:Products_Category",
                        Products_Price="params:Products_Price",
                        #Products_SalesDate="params:Products_SalesDate",
                        ),
            outputs="Products",
            tags=["products"]
        ),
    ],
    namespace = "Products"
    )

    inventory_stock_pipeline = pipeline([
        node(
            func=list_columns,
            inputs=dict(Stock="Stock_",
                        Stock_ProductID="params:Stock_ProductID",
                        Stock_Quantity="params:Stock_Quantity",                        
                        ),
            outputs="Stock",
            tags=["stock"]
        ),
    ],
    namespace = "Stock")

    inventory_pipeline = pipeline(
        pipe = inventory_products_pipeline + inventory_stock_pipeline,
     namespace= "Inventory")

    return inventory_pipeline


def list_columns(**kwargs):
    return kwargs
