#!/usr/bin/python3
import re

string = "Example string containing Title (2022), [Verse 1] some lyrics, @username, ISBN 1234-5-678-90123-4, Why did the joke? Because..., Show Name S01E01: Episode Title, 01-Jan-2023, #ABC123, 192.168.0.1"

pattern =".+ \(\d{4}\)"
result=re.findall(pattern, string)
print(result)
