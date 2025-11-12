import re

data = "1123123 {asdf asdf dasf}"

print(re.search(r'\d+|\{.*\}', data).group())