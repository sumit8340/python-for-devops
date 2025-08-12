import re

text = "The quick brown fox." # match only match when the string is started with quick
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
