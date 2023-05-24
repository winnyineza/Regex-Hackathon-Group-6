#!/usr/bin/python3

import re

string = """
Movie: "Game of thrones (2011), House of dragons (2022),
Song: [Verse 1] I can't hide myself I don't expect you understand I just hope I can explain What it's like to be a man It's a lonely road,
Twitter: @DenmarkEddy
ISBN: ISBN 123-4-567-89012-3
Joke: Why did the chicken cross the road? Because it wanted to get to the other side, Why did the seagulls fly over the ocean? Because if they flew over the bay
TV Episode: Show Name S01E02: Episode Title
Date: 24-May-2023
Color: #FF0000
IP Address: 192.168.0.1
"""
pattern = r"Joke: (Why did the .+\? Because.+)"

result = re.findall(pattern, string)
print(result)
