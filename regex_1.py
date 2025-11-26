import re

def find_emails(text):
    """
    Find all email addresses in the given text.

    Args:
        text (str): The input text to search for email addresses.
    Returns:
        list: A list of found email addresses.
    """

    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)


txt = "Please contact us at support@example.com for assistance."

emails = find_emails(txt)
print(emails)