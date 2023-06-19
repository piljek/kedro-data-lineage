from kedro.pipeline import Pipeline, node
import pandas as pd


def create_pipeline(**kwargs) -> Pipeline:
    
    pipeline = Pipeline([
        node(
            func=avg_order_value,
            inputs=dict(
                sales="Sales",
                Sales_SalesValue = "params:Sales_SalesValue",
                Sales_OrderID = "params:Sales_OrderID",
            ),
            outputs="Sales_Order_Value_AVG"
        ),
        node(
            func=product_order_value,
            inputs=dict(
                sales="Sales",
                Sales_SalesValue = "params:Sales_SalesValue",
                Products_ProductID="params:Products_ProductID",
            ),
            outputs="Sales_Product_Order_Value",
                    tags=["sales", "products", "stock"]

        )
    ])

    return pipeline

def avg_order_value(sales: pd.DataFrame, Sales_SalesValue, Sales_OrderID) -> float:
    # Calculate the sum of sales
    total_sales = sales[Sales_SalesValue].sum()

    # Count the total number of distinct orders
    total_orders = sales[Sales_OrderID].nunique()

    # Average the sales 
    # Avoid dividing by 0
    if total_orders == 0:
        return total_sales
    else:
        # Average the sales y the number of 
        return total_sales/total_orders
    

def product_order_value(sales, Sales_SalesValue, Products_ProductID):
    # Calculate the sales per product
    product_sales = sales.groupby(Products_ProductID)[Sales_SalesValue].sum()

    # Rank the product sales from high to low
    top_product_sales = product_sales.sort_values(ascending=False)
    return top_product_sales
