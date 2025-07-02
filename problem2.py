import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders=orders.groupby('customer_number')['order_number'].nunique().reset_index().sort_values(by=['order_number'],ascending=False).head(1)
    return orders[['customer_number']]