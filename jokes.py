#!/usr/bin/python3

import re

    string = "Games Of Throne (2011), [Verse 1] I can't hide myself I don't expect you to understand I just hope I can explain What it's like to be a man It's a lonely road And they don't care 'bout what you know It's not 'bout how you feel But what you provide inside that home, @DenmarkEddy, ISBN 1234-5-678-90123-4, Why did the joke? Because..., Games Of Throne S01E01: Episode Title, 01-Jan-2023, #ABC123, 192.168.0.1"
    pattern = r"Joke: (Why did the .+\? Because.+)"

    result = re.findall(pattern, string)

    print(result)
