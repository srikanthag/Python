# Regular expressions (regex) are a powerful tool for pattern matching and text manipulation. Python's `re` module provides 
# functions to work with regexes.

# 1. Basic Matching
import re
# Define a regex pattern for a phone number
pattern = r'\d{3}-\d{3}-\d{4}'
text = 'Call me at 123-456-7890 or 987-654-3210.'

matches = re.findall(pattern, text)
print("Phone numbers found:", matches)


# 2. Email Validation
import re
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
email = 'example.email@domain.com'

if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")


# 3. Extracting Dates
import re
pattern = r'\b\d{2}/\d{2}/\d{4}\b'
text = 'The deadlines are 12/15/2024 and 01/20/2025.'

dates = re.findall(pattern, text)
print("Dates found:", dates)


# 4. Replacing Text
import re
pattern = r'foo'
text = 'foo bar foo baz'

# Replace 'foo' with 'qux'
replaced_text = re.sub(pattern, 'qux', text)
print("Replaced text:", replaced_text)


# 5. Splitting Text
import re

text = 'Python is awesome!  It is so much fun.'
pattern = r'\s+'
words = re.split(pattern, text)
print("Words:", words)


# 6. Finding All Matches with Groups
import re

pattern = r'(\d{2})/(\d{2})/(\d{4})'
text = 'Important dates: 12/15/2024, 01/20/2025.'

matches = re.findall(pattern, text)
for match in matches:
    month, day, year = match
    print(f"Month: {month}, Day: {day}, Year: {year}")


# 7. Checking for a Pattern at the Beginning or End of a String
import re

text = 'Hello world'
pattern = r'^Hello'

if re.match(pattern, text):
    print("The string starts with 'Hello'")
else:
    print("The string does not start with 'Hello'")


# 8. Using Regex with Case Insensitivity
import re

text = 'Python is Fun'
pattern = r'python'

matches = re.findall(pattern, text, re.IGNORECASE)
print("Matches found:", matches)
