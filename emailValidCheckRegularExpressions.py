import re
pattern = r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$"
def is_valid_email(email):
    return bool(re.match(pattern,email))
print(is_valid_email("anu.kumar@college.edu"))
print(is_valid_email("bad-email@@x"))
print(is_valid_email("no-at-symbol.com"))
