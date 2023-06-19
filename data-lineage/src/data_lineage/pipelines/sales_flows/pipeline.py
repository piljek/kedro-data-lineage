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
            tags=["sales", "customers", "sales_customers_flow"],
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
            tags=["sales", "products", "sales_products_flow"]
        ),
        node(
        func=sales_products_stock_flow,
        inputs=dict(
            Sales= "Sales",
            Products = "Products",    
            Stock = "Stock",
            # sales attributes:
            Sales_OrderID = "params:Sales_OrderID",

            # product attributes
            Products_ProductName="params:Products_ProductName",
            Products_Category="params:Products_Category",
            Products_Price="params:Products_Price",

            # stock attributes
            Stock_ProductID = "params:Stock_ProductID",
            Stock_Quantity = "params:Stock_Quantity",
        ),
        outputs= "Sales Products Stock Flow",
        tags=["sales", "products", "stock", "sales_products_stock_flow"]
        ),
    ],
        # namespace="data_processing",
        # inputs=["companies", "shuttles", "reviews"],
        # outputs="model_input_table",
        )

    return pipeline


def sales_customers_flow(**kwargs):
    return kwargs
def sales_products_flow(**kwargs):
    return kwargs
def sales_products_stock_flow(**kwargs):
    return kwargs
