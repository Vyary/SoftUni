import re


class EmailMustStartWithLetterError(Exception):
    "Raised if name doesn't start with a letter"
    pass


class NameTooShortError(Exception):
    "Raised if name if shorter than 4 characters"
    pass


class MustContainAtSymbolError(Exception):
    "Raised if email doesn't contain @ symbol"
    pass


class TooManyAtSymbolsError(Exception):
    "Raised if email contains too many @ symbols"
    pass


class InvalidDomainNameError(Exception):
    "Raised if email domain name is invalid"
    pass


class InvalidDomainError(Exception):
    "Raised if domain end doesn't end with .com, .bg, .org or .net"
    pass


class TooManyDots(Exception):
    "Raised if there are more than one dot between domain name and ending"
    pass


# regular expressions:

# regex for email name
# must starts with a letter
pattern_email_start = r"^[a-zA-Z]"

# regex for email name
# followed by letters, numbers, dots, hyphens, and underscores
pattern_email_name = r"([a-z0-9\-\.\_]+)@"

# regex for domain name
# after the @ symbol (must contain lowercase letters, numbers, and hyphens) ends with .
pattern_email_domain = r"@([a-z\-0-9]+)\."

# regex for domain ending
# must end with .com, .bg, .org, or .net
pattern_email_end = r"(.com|.bg|.org|.net)$"

# regex for domain name + end
pattern_domain = r"@([a-z\-0-9]+)(.com|.bg|.org|.net)$"

while True:
    email = input()
    if email == "End":
        break

    elif "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    elif (
        re.search(pattern_email_name, email) is None
        or len(re.search(pattern_email_name, email).group(1)) <= 4
    ):
        raise NameTooShortError("Name must be more than 4 characters")

    elif re.search(pattern_email_start, email) is None:
        raise EmailMustStartWithLetterError("Email must start with a letter")

    elif email.count("@") > 1:
        raise TooManyAtSymbolsError("Email contains too many @ symbols")

    elif re.search(pattern_email_domain, email) is None:
        raise InvalidDomainNameError("Email domain name is invalid")

    elif re.search(pattern_email_end, email) is None:
        raise InvalidDomainError(
            "Domain must be one of the following: .com, .bg, .org, .net"
        )

    elif re.search(pattern_domain, email) is None:
        raise TooManyDots("Too many dots between domain name and domain ending")

    else:
        print("Email is valid")


"""                     Task:
You will be given some emails until you receive the command "End".
Create the following custom exceptions to validate the emails:
•	NameTooShortError - raise it when the name in the email is less than or
equal to 4 ("peter" will be the name in the email "peter@gmail.com")
•	MustContainAtSymbolError - raise it when there is no "@" in the email
•	InvalidDomainError - raise it when the domain of the email is invalid
(valid domains are: .com, .bg, .net, .org)
When an error is encountered, raise it with an appropriate message:
•	NameTooShortError - "Name must be more than 4 characters"
•	MustContainAtSymbolError - "Email must contain @"
•	InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"
Hint: use the following syntax to add a message to the Exception:
MyException("Exception Message")
If the current email is valid, print "Email is valid" and read the next one

Example:
Input:
abc@abv.bg
Output:
Traceback (most recent call last):
  File "./email_validator.py", line 20, in <module>
    raise NameTooShort("Name must be more than 4 characters")
__main__.NameTooShort: Name must be more than 4 characters

Example2:
peter@gmail.com
petergmail.com
Output:
peter@gmail.com
petergmail.com	Email is valid
Traceback (most recent call last):
  File "./email_validator.py", line 18, in <module>
    raise MustContainAtSymbolError("Email must contain @")
__main__.MustContainAtSymbolError: Email must contain @
"""
