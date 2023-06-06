"""
This is a boilerplate pipeline 'products'
generated using Kedro 0.18.9
"""

from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:

    pipeline = Pipeline([
        node(
            func=list_columns,
            inputs=dict(Products="Products_",
                        Products_ProductID="params:Products_ProductID",
                        Products_ProductName="params:Products_ProductName",
                        Products_Category="params:Products_Category",
                        Products_Price="params:Products_Price",
                        Products_SalesDate="params:Products_SalesDate",
                        ),
            outputs="Products",
            tags=["products"]
        ),
        node(
            func=list_columns,
            inputs=dict(Products="Stock_",
                        Stock_ProductID="params:Stock_ProductID",
                        Stock_QuantityAvailability="params:Stock_QuantityAvailability",                        
                        ),
            outputs="Stock",
            tags=["stock"]
        ),
    ])
    return pipeline


def list_columns(**kwargs):
    return kwargs
