"""
This is a boilerplate pipeline 'sales_customer_flow'
generated using Kedro 0.18.9
"""

from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:

    sales_customer_view = pipeline([
        node(
            func=sales_customers_flow,
            inputs=dict(
                Sales="Sales",
                Customers="Customers",
                Sales_OrderID="params:Sales_CustomerID",
                Customers_OrderID="params:Customers_CustomerID",
            ),            
            outputs="sales_customer_view_out",
            tags=["sales", "customers", "sales_customers_flow"],
        ),
    ],
        # namespace = "SalesCustomer"
    )
    sales_products_view = pipeline([
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
            outputs="sales_products_view_out",
            tags=["sales", "products", "sales_products_flow"]
        ),
    ],
        # namespace = "SalesProducts"
    )
    sales_products_stock_view = pipeline([

        node(
            func=sales_products_stock_flow,
            inputs=dict(
                Sales="Sales",
                Products="Products",
                Stock="Stock",
                # sales attributes:
                Sales_OrderID="params:Sales_OrderID",

                # product attributes
                Products_ProductName="params:Products_ProductName",
                Products_Category="params:Products_Category",
                Products_Price="params:Products_Price",

                # stock attributes
                Stock_ProductID="params:Stock_ProductID",
                Stock_Quantity="params:Stock_Quantity",
            ),
            outputs="sales_products_stock_flow_out",
            tags=["sales", "products", "stock", "sales_products_stock_flow"]
        ),
    ],
    )

    p_sales_customer_view = pipeline(
        pipe=sales_customer_view,
        inputs={"Sales": "Sales", "Customers": "Customers"},
        outputs={"sales_customer_view_out": "Sales Customer Projection"},
        namespace="Sales_Customers"
    )
    p_sales_products_view = pipeline(
        pipe=sales_products_view,
        inputs={"Sales": "Sales", "Products": "Products"},
        outputs={"sales_products_view_out": "Sales Products Projection"},
        namespace="Sales_Products"
    )
    p_sales_products_stock = pipeline(
        pipe=sales_products_stock_view,
        inputs={"Sales": "Sales", "Products": "Products", "Stock": "Stock"},
        outputs={"sales_products_stock_flow_out": "Sales Products Stock Projection"},
        namespace="Sales_Products_Stock"
    )

    projection_pipeline = pipeline(
        # sales_customer_view + sales_products_view + sales_products_stock_view,
        pipe= p_sales_customer_view + p_sales_products_view + p_sales_products_stock,
        namespace="Projections",
        inputs={"Sales": "Sales.Sales",
                "Products": "Inventory.Products.Products", "Stock": "Inventory.Stock.Stock",
                "Customers":"Customer.Customers"}
    )

    return projection_pipeline


def sales_customers_flow(**kwargs):
    return kwargs


def sales_products_flow(**kwargs):
    return kwargs


def sales_products_stock_flow(**kwargs):
    return kwargs
