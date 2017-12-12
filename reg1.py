import re
def text_match(text):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns,text):
        return "valid"
    else:
        return "non valid"
print(text_match("aaa_bbc"))
