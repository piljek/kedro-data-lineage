"""
This is a boilerplate pipeline 'customers'
generated using Kedro 0.18.9
"""

from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:

    customer_pipeline = pipeline([
        node(
            list_columns,
            inputs=dict(
                Customers="Customers_",  # Customers data,
                # Customer Columns:
                Customers_CustomerID="params:Customers_CustomerID",
                Customers_FirstName="params:Customers_FirstName",
                Customers_LastName="params:Customers_LastName",
                Customers_Email="params:Customers_Email",
            ),
            outputs="Customers",
            tags=["customers"]
        ),
    ],
    namespace = "Customer")
    return customer_pipeline


def list_columns(**any):
    return
