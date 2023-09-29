import datetime
import csv
import pandas as pd
import re
import logging
import requests
import time

from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path


from config import headers, csv_file_path
from notify import EmailNotify as en
from log import get_logger


class ScrapeData():
    def __init__(self):
        pass

    def check_price(self, df: pd.DataFrame, product_url: str, price_threshold: float) -> bool:
        """
        Check the price of a product against a price threshold.

        Args:
            df (pd.DataFrame): The DataFrame containing the product data.
            product_url (str): The URL of the product.
            price_threshold (float): The price threshold to compare against.

        Returns:
            bool: True if the price is under the threshold, False otherwise.
        """
        try:
            result_df = df.query(
                f"product_url == '{product_url}' and {price_threshold} > product_price")
        except pd.errors.EmptyDataError:
            get_logger().warning("No data found for the given product URL.")
            return False

        if not result_df.empty:
            get_logger().info("Price is Under the threshold.")
            print("Price is Under the threshold.")
            return True
        else:
            get_logger().info("Price is not Under the threshold.")
            print("Price is not Under the threshold.")
            return False

    def insert_data_csv(self, product_url: str, product_name: str, product_price: float, price_threshold: float, email: str):
        """
        Inserts data into a CSV file.

        Args:
            product_url (str): The URL of the product.
            product_name (str): The name of the product.
            product_price (float): The price of the product.
            price_threshold (float): The threshold price for notification.
            email (str): The email address for notification.

        Returns:
            None
        """
        data = {
            'product_url': product_url,
            'product_name': product_name,
            'product_price': product_price,
            'date': datetime.utcnow()
        }

        df = pd.DataFrame(data, index=[0])

        csv_file = Path(csv_file_path)

        flag = self.check_price(df, product_url, price_threshold)

        if csv_file.exists() and csv_file.is_file():
            existing_df = pd.read_csv(csv_file)
            df = pd.concat([existing_df, df], ignore_index=True)

        df.to_csv(csv_file_path, index=False)
        get_logger().info("Data has been added to the CSV file.")

        if flag:
            get_logger().info("Notifying the user via Email")
            en.notify_email(product_name, product_url, price_threshold, email)
        else:
            time.sleep(86400)  # For 1 Week
            if product_url and price_threshold and email:
                self.extract_data(product_url, price_threshold, email)
            else:
                get_logger().warning("Missing required data for extraction.")

    def extract_data(self, product_url: str, price_threshold: float, email: str):
        """
        Extracts data from a given product URL and inserts it into a CSV file.

        Parameters:
            product_url (str): The URL of the product.
            price_threshold (float): The price threshold for the product.
            email (str): The email to notify when the price falls below the threshold.

        Raises:
            ValueError: If any of the required data (product URL, product name, product price) is missing.
            Exception: If an error occurs during the extraction process.

        Returns:
            None
        """

        try:
            page = requests.get(product_url, headers=headers)
            soup1 = BeautifulSoup(page.content, features='lxml')
        except requests.exceptions.RequestException as e:
            # Handle network-related errors (e.g., connection issues, timeouts)
            print(f"Network error: {e}")

        product_name = soup1.find(
            'span', attrs={'id': 'productTitle'}).getText().strip()
        product_price = soup1.find(
            'span', attrs={'class': 'a-price-whole'}).getText().strip()

        # convert product_price into int type
        product_price = float("".join(re.findall(r"[\d\.]+", product_price)))

        get_logger().info("Data has been extracted successfully from the provided URL.")

        if product_url and product_name and product_price:
            self.insert_data_csv(product_url, product_name,
                                 product_price, price_threshold, email)
        elif product_url is None or product_name is None or product_price is None:
            raise ValueError("Missing data")
        else:
            raise Exception(f"An error occurred {e}")
