import os
import sqlite3

from langchain_core.tools import tool
from prompt import product_prompt, guarantee_prompt

@tool
def customer_order_checking(order_id: str = None, tracking_number: str = None):
    """
    Tools to check customer order status, location, etc.

    Args:
        order_id (str, optional): unique number to identify the order transaction, consist of 3 digits.
        tracking_number (str, optional): unique code to monitor the package transit progress.
    """

    results = []
    filter_query = []
    value = []
    conn = sqlite3.connect(os.getenv('DB_PATH'))

    query = """
    SELECT id, order_id, tracking_number, customer_location, order_current_location, product_name, order_status, estimated_time_arrival
    FROM orders
    """

    if order_id:
        filter_query.append("order_id = ?")
        value.append(order_id.upper())
    
    if tracking_number:
        filter_query.append("tracking_number = ?")
        value.append(tracking_number.upper())
    
    if filter_query:
        query += " WHERE " + " OR ".join(filter_query) + ";"

    with conn:
        cursor = conn.cursor()
        cursor.execute(query, value)
        rows = cursor.fetchall()

        header = [desc[0] for desc in cursor.description]

        results = [dict(zip(header, row)) for row in rows]

    return results


@tool
def claim_guarantee() -> str:
    """
    Tools if the question asking about guarantee claim of the product.
    How to claim product guarantee.
    No need an Arguments.
    """
    return guarantee_prompt

@tool
def info_product() -> str:
    """
    Tools if the question asking about product, it can be pros or price or description.
    No need an Arguments.
    """
    return product_prompt