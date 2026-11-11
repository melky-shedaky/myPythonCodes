#Compile Comparsion
import re
#Compile Once
ip_pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
#reuse many Times -- Faster than Calling re.findall() Repeatedly
log_lines = ["Requested From 192.168.1.10","BLocked 10.1.0.52", "Ok 126.63.09.555","6.5.42. ", "1.2.3"]
for line in log_lines:
    match = ip_pattern.search(line)
    if match:
        print(match.group())
