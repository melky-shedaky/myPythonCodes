#Regular Expression Or validations
import re
text = "order #4521 Shipped, order #78 Pending, order #903 Done"
#Without Regex: You'd need custom Loops to FInd Every Order #<Digits>
#with Regex: one line Describes The Patterns
orders = re.findall(r"order #\d+",text)
print(orders)
