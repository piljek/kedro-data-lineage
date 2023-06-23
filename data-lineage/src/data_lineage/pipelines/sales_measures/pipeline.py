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
            func=top_products,
            inputs=dict(
                # sales="Sales.Sales",
                Sales_Measures="Sales_Measures",
                Sales_SalesValue="params:Sales_SalesValue",
                Products_ProductID="params:Products_ProductID",
                n= "params:n_top_products"
            ),
            outputs="Sales_Product_Order_Value_out",
                    tags=["sales", "products", ]

        )
    ]  # ,namespace="Sales_Measures",
    )

    measure_pipeline = pipeline(
        pipe=sales_measure_pipeline,
        inputs={"Sales_Measures": "Projections.Sales Products Projection"},
        namespace="Sales_Measures",
        outputs={"Sales_Order_Value_AVG_out": "Sales_Order_Value_AVG",
                 "Sales_Product_Order_Value_out": "Sales_Product_Order_Value"}
    )

    return measure_pipeline


def avg_order_value(Sales_Measures: pd.DataFrame,
                    Sales_SalesValue: str,
                    Sales_OrderID: str) -> float:
    """
    Calculate the Average Order Value.

    Parameters:
        - Sales_Measures(pd.DataFrame): DataFrame containing the sales
            and order data with columns 'OrderID' and 'SalesValue'.
        - Sales_SalesValue (str): Column name to calculate the sales amount
        - Sales_OrderID (str): Column name to group and calculate the 
            sales amount per order

    Returns:
        - float: Average Order Value rounded to 2 decimal places.
    """

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
        return round(total_sales/total_orders, 2)


def top_products(Sales_Measures: pd.DataFrame,
                        Sales_SalesValue: str,
                        Products_ProductID: str,
                        n: int) -> pd.DataFrame:
    """
    Calculate the top n sales products based on quantity sold.

    Args:
        Sales_Measure (DataFrame): The data frame containing 
          the product and sales information.
        Sales_SalesValue (str): The sales amount column that sums
          the sales
        Products_ProductID (str): The product id column the dataframe
          is grouped by
        n (int): The number of top products to return.

    Returns:
        DataFrame: The top n sales products sorted by quantity sold.
    """

    # Calculate the sales per product
    product_sales = Sales_Measures.groupby(Products_ProductID)[
        Sales_SalesValue].sum()

    # Rank the product sales from high to low
    top_products = product_sales.nlargest(n)
    return top_products
