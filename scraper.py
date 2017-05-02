import re

import requests
from bs4 import BeautifulSoup

INSPECTION_DOMAIN = 'http://info.kingcounty.gov'
INSPECTION_PATH = '/health/ehs/foodsafety/inspections/Results.aspx'
INSPECTION_PARAMS = {
    'Output': 'W',
    'Business_Name': '',
    'Business_Address': '',
    'Longitude': '',
    'Latitude': '',
    'City': '',
    'Zip_Code': '',
    'Inspection_Type': 'All',
    'Inspection_Start': '',
    'Inspection_End': '',
    'Inspection_Closed_Business': 'A',
    'Violation_Points': '',
    'Violation_Red_Points': '',
    'Violation_Descr': '',
    'Fuzzy_Search': 'N',
    'Sort': 'H'
}


def get_inspection_page(**kwargs):
    """
    Given a set of inspection parameters, return an inspection page.

    This function shoud:

      * accept keyword arguments for each of the possible query values
      * build a dictionary of request query parameters from incoming keywords, using INSPECTION_PARAMS as a template
      * make a request to the inspection service search page using this query
      * return the unicode-encoded content of the page
    """

    arguments = INSPECTION_PARAMS.copy()  # Use the kwargs dictionary to replace the defaults arguments in arguments
    for key, val in kwargs.items():
        if key in INSPECTION_PARAMS:
            arguments[key] = val

    # Combine the domain and path to make the URL the URL
    url = INSPECTION_DOMAIN + INSPECTION_PATH

    resp = requests.get(url, params=arguments)

    return resp.text


def parse_source(html):
    """
    Returns a BeautifulSoup object, given the html
    """

    return BeautifulSoup(html, "html5lib")


def restaurant_data_generator(html):
    """
    Given a BeautifulSoup instance return a find_all generator
    with only the restaurant data divs.
    """

    id_finder = re.compile(r'PR[\d]+~')
    return html.find_all('div', id=id_finder)


def has_two_tds(elem):
    """
    Predicate which reports if a BeautifulSoup element is a table
    row which has exactly two tds.
    """

    pass


def clean_data(td):
    """
    Given a td, return its text, after stripping away newlines, spaces,
    colons, and dashes.
    """

    pass


def extract_restaurant_metadata(elem):
    pass


def is_inspection_data_row(elem):
    pass


def get_score_data(elem):
    pass


def result_generator(count):
    pass


if __name__ == '__main__':
    results = get_inspection_page(Inspection_Start="12/7/2001",
                                  Inspection_End="12/7/2002"
                                  )
    parsed = parse_source(results)
    info_divs = restaurant_data_generator(parsed)

    print(info_divs)
