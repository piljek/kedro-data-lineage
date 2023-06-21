from kedro.pipeline import Pipeline, node, pipeline
import pandas as pd


def create_pipeline(**kwargs) -> Pipeline:

    sales_measure_pipeline = pipeline([
        node(
            func=avg_order_value,
            inputs=dict(
                Sales_Measures="Sales_Measures",
                Sales_SalesValue="params:Sales.Sales_SalesValue",
                Sales_OrderID="params:Sales_OrderID",
            ),
            outputs="Sales_Order_Value_AVG_out"
        ),
        node(
            func=product_order_value,
            inputs=dict(
                # sales="Sales.Sales",
                Sales_Measures="Sales_Measures",
                Sales_SalesValue="params:Sales.Sales_SalesValue",
                Products_ProductID="params:Inventory.Products.Products.Products_ProductID",
            ),
            outputs="Sales_Product_Order_Value_out",
                    tags=["sales", "products", "stock"]

        )
    ]#,namespace="Sales_Measures",
    )

    measure_pipeline = pipeline(
        pipe=sales_measure_pipeline,
        inputs={"Sales_Measures": "Projections.Sales Products Projection"},
        namespace="Sales_Measures",
        outputs={"Sales_Order_Value_AVG_out": "Sales_Order_Value_AVG", "Sales_Product_Order_Value_out" : "Sales_Product_Order_Value"}
    )

    return measure_pipeline


def avg_order_value(Sales_Measures: pd.DataFrame, Sales_SalesValue, Sales_OrderID) -> float:
    # Calculate the sum of sales
    total_sales = Sales_Measures[Sales_SalesValue].sum()

    # Count the total number of distinct orders
    total_orders = Sales_Measures[Sales_OrderID].nunique()

    # Average the sales
    # Avoid dividing by 0
    if total_orders == 0:
        return total_sales
    else:
        # Average the sales y the number of
        return total_sales/total_orders


def product_order_value(Sales_Measures, Sales_SalesValue, Products_ProductID):
    # Calculate the sales per product
    product_sales = Sales_Measures.groupby(Products_ProductID)[Sales_SalesValue].sum()

    # Rank the product sales from high to low
    top_product_sales = product_sales.sort_values(ascending=False)
    return top_product_sales
