import re
text = "this is Is a simple siMPle test of OF regex"
#\1 refers back to whateveer group 1 mathced --  a repeated word check
pattern = r"\b(\w+)\s+\1\b"
repeats = re.findall(pattern, text, flags=re.IGNORECASE)
print("Repeated words Found:",repeats)
