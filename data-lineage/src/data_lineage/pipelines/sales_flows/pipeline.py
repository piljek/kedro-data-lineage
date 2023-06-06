"""
This is a boilerplate pipeline 'sales_customer_flow'
generated using Kedro 0.18.9
"""

from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:

    pipeline = Pipeline([
        node(
            func=sales_customers_flow,
            inputs=dict(
                Sales="Sales", 
                Customers="Customers",
                Sales_OrderID="params:Sales_CustomerID",
                Customers_OrderID="params:Customers_CustomerID",
            ),
            outputs="Sales Customer Flow",
            tags=["sales", "customers"]
        ),
        node(
        sales_products_flow,
        inputs=dict(
                Sales="Sales", 
                Products="Products",
                Sales_OrderID="params:Sales_CustomerID",
                Products_ProductName="params:Products_ProductName",
                Products_Category="params:Products_Category",
                Products_Price="params:Products_Price",




            ),
            outputs="Sales Products Flow",
            tags=["sales", "products"]
        )
    ])

    return pipeline


def sales_customers_flow(**kwargs):
    return kwargs
def sales_products_flow(**kwargs):
    return kwargs
