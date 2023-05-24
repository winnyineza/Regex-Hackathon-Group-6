#!/usr/bin/python3

import re

def extract_usernames(input_string):
    pattern = r'@[\w\d]+'
    matches = re.findall(pattern, input_string)
    return matches

input_string = "Hello @username1, how are you doing? Did you see @user2's latest post?"

usernames = extract_usernames(input_string)

for username in usernames:
    print(username)
