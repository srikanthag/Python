numbers = ['857', '987', '8', '120', '888888', '547', '7674', '89', '589', '388888', '2889']
import re
for item in numbers:
    d = re.sub(r'857', '5555', item)
    print(d)




































