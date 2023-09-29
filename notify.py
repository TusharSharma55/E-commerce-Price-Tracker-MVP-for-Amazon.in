import smtplib
import ssl

from config import smtp_port, smtp_server, email_from, password
from log import get_logger


class EmailNotify():
    def notify_email(product_name: str, product_url: str, price_threshold: float, email: str):
        """
        Sends an email notification to the specified email address when the price of a product drops below a certain threshold.

        Args:
            product_name (str): The name of the product.
            product_url (str): The URL of the product.
            price_threshold (float): The price threshold below which the notification will be sent.
            email (str): The email address to send the notification to.

        Returns:
            None
        """

        email_to = email

        # content of message
        subject = f"The {product_name} you want is under Rs{price_threshold}! Now is your chance to buy!"
        body = f"Buddy, This is the moment we have been waiting for. \n Now is your chance to pick up the {product_name} of your dreams. \n\n Don't mess it up! Link here: {product_url}"

        message = f"Subject: {subject}\n\n{body}"

        # Create context
        simple_email_context = ssl.create_default_context()

        try:
            # Connect to the server
            print("Connecting to server...")
            get_logger().info("Connecting to server...")
            TIE_server = smtplib.SMTP(smtp_server, smtp_port)
            TIE_server.starttls(context=simple_email_context)
            TIE_server.login(email_from, password=password)
            print("Connected to server :-)")
            get_logger().info("Connected to server :-)")

            # Send the actual email
            print()
            get_logger().info(f"Sending email to - {email_to}")
            print(f"Sending email to - {email_to}")
            TIE_server.sendmail(email_from, email_to, message)
            get_logger().info(f"Email successfully sent to - {email_to}")
            print(f"Email successfully sent to - {email_to}")

        except Exception as e:
            get_logger().error(e)

        # Close the port
        finally:
            TIE_server.quit()
