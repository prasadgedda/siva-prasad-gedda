import re

def is_valid_email(s):
    pattern = r'^[\w.]+@[A-Za-z0-9-]+\.[A-Za-z]{2,6}$'
    return re.fullmatch(pattern, s) is not None


valid_emails = [
    "user@gmail.com",
    "john.doe@example.com",
    "abc123@test.in",
    "hello_world@domain.co"
]

invalid_emails = [
    "a@b.c",
    "a\@b.c",
    "no-at-sign.com",
    "user@gmail"
]

for email in valid_emails:
    print(email, "->", is_valid_email(email))

for email in invalid_emails:
    print(email, "->", is_valid_email(email))
#output
    #user@gmail.com -> True
#john.doe@example.com -> True
#abc123@test.in -> True
#hello_world@domain.co -> True
#a@b.c -> False
#a\@b.c -> False
#no-at-sign.com -> False
#user@gmail -> False
