# E-commerce Price Tracker MVP for Amazon.in

The E-commerce Price Tracker MVP is a terminal-based Python application designed to scrape product prices from a specified Amazon.in product URL and notify users via email when prices drop below a specified threshold.

Users can input the Amazon.in product URL, their email address and the specified price threshold for notifications through the terminal.

## Tech Stack

- [Python](https://docs.python.org/3/) - Terminal based Python application
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Used For Web Scrapping.
- [smptlib](https://docs.python.org/3/library/smtplib.html) - For sending email to any internet machine
- [Validators](https://validators.readthedocs.io/en/latest/) - For Validating the URL provided by the user.

## Package manager - pip

This project is using `pip` as package manager, if you do not have this installed on your machine please start by looking at the [pip docuentation and tutorials](https://pip.pypa.io/en/stable/cli/pip_install/).
Clone this git Repo through your terminal.

# How to run this project

After installing the package manager and clonning the project following commands will be run by you in terminal:

To Move in app directory

```sh
cd app
```

Create a Virtual Environment

```sh
python -m venv env
```

To activate Virtual Environment

```sh
source env/bin/activate
```

To install all the project requirements/dependencies

```sh
pip install -r requirements.txt
```

Then Simply Run the project

- \*Product_URL and Email Address must be Quoted
- \*Price Threshold in int.

```sh
python main.py {Your Amazon Product URL} {Your Email Address} {Price Threshold}
```

# Project structure in app

```
├───AllLogs/
│   ├───log_details.log
├───Store/
│   ├───newProduct.csv
│──config.py
│───log.py
│───logging_config.py
├───main.py
├───notify.py
├───scrape.py
├───requirements.txt
└───.gitignore
```

**log_details.log** - This contains all the records created during the project's execution.

**newProduct.csv** - A CSV file that contains information about product URLs, product names, product prices, and dates..

**requirements.txt** - This list includes all the Python libraries used in this project..
