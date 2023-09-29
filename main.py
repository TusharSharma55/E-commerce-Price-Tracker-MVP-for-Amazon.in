import argparse
import re
import validators

from scrape import ScrapeData as sd


def is_valid_url(url):
    """
    Check if a given URL is valid.

    Parameters:
        url (str): The URL to be validated.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    return validators.url(url)


def is_valid_email(email):
    """
    Check if the given email is valid.

    Parameters:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)


def main():
    """
    Parse command line arguments and execute the E_Commerce Product URL Price Tracker.

    Args:
        product_url (str): Amazon.in product URL.
        email (str): Email address.
        price_threshold (int): Price Threshold in Rs.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(
        description="E_Commerce Product URL Price Tracker, Email, and PriceThreshold Input")

    parser.add_argument('product_url', type=str, help="Amazon.in product URL")
    parser.add_argument('email', type=str, help="Email address")
    parser.add_argument('price_threshold', type=int,
                        help="Price Threshold in Rs.")

    args = parser.parse_args()

    if is_valid_url(args.product_url) and is_valid_email(args.email):
        sd().extract_data(args.product_url, args.price_threshold, args.email)
    else:
        print("Error: Missing one or more entries (product URL, email, or age).")


if __name__ == "__main__":
    main()
