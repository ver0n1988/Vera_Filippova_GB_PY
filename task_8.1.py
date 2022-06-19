import re


VALID_RE = re.compile(
    r'(?P<username>[a-zA-Z0-9\.\-\_]+)@(?P<domain>[a-zA-Z0-9\.\-\_]+)')


def email_parse(email_address):
    """ validation of email """
    try:
        test = map(lambda x: x.groupdict(), VALID_RE.finditer(email_address))
        print(test.__next__())
    except:
        raise ValueError from ValueError