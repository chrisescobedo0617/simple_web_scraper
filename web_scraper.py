import requests
import sys
import argparse
import re


def get_emails(url):
    """Function to return a list of emails without duplicates"""
    response = requests.get(url)
    text_response = response.text
    email_list = re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', text_response)
    emails = {}
    unique_emails = []
    for email in email_list:
        if emails.get(email) == None:
            emails[email] = 1
    for key, value in emails.items():
        if 1 == value:
            unique_emails.append(key)
    print('Emails:')
    print('\n')
    if not unique_emails:
        print('NONE')
    else:
        for email in unique_emails:
            print(email)

def get_phone_numbers(url):
    """Function to return a list of phone numbers without duplicates"""
    response = requests.get(url)
    text_response = response.text
    phone_number_list = re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', text_response)
    phone_numbers = {}
    unique_phone_numbers = []
    for phone_number in phone_number_list:
        if phone_numbers.get(phone_number) == None:
            phone_numbers[phone_number] = 1
    for key, value in phone_numbers.items():
        if 1 == value:
            unique_phone_numbers.append(key)
    print('Phone Numbers:')
    print('\n')
    if not unique_phone_numbers:
        print('NONE')
    else:
        for phone_number in unique_phone_numbers:
            print(phone_number)


def get_urls(url):
    """Function to return a list of urls without duplicates"""
    response = requests.get(url)
    text_response = response.text
    url_list = re.findall(r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)", text_response)
    urls = {}
    unique_urls = []
    for url in url_list:
        if urls.get(url) == None:
            urls[url] = 1
    for key, value in urls.items():
        if 1 == value:
            unique_urls.append(key)
    print('URLS:')
    print('\n')
    if not unique_urls:
        print('NONE')
    else:
        for url in unique_urls:
            print(url)


def create_parser():
    """Create a command line parser object with some arguments."""
    parser = argparse.ArgumentParser(
        description="Returns a list of emails, urls, and phone numbers from a given url.")
    parser.add_argument(
        'url', help='URL to search for emails, urls, and phone numbers')
    return parser


def main(args):
    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args()

    url = ns.url

    if not ns:
        parser.print_usage()
        sys.exit(1)
    get_emails(url)
    print('\n')
    get_phone_numbers(url)
    print('\n')
    get_urls(url)

if __name__ == '__main__':
    main(sys.argv[1:])