import re

response = "Here is the song lyrics: [Verse 1] They call me Burna Boy Oh, oh, oh, oh See, ever since I walked in You've been talking and talking and talking Ding, ding, ding, ding, ding, ding, ding, ding Booh! Aye!, [Verse 2] You and I are not the same We are very, very different So don't try to act like my friend Like you knew me from back... when? Na na na na na! Try not to bother 'bout ma character Instead of asking questions like a barrister You should have gone straight to my manager You go listen carefully My brother I know about me I'on know 'bout the others But if anybody diss my mother, @Inezawinny"

pattern =  r"\[(Verse \d+)\] ([^,]+)"

matches = re.findall(pattern, response)

for match in matches:
    verse_number = match[0]
    lyrics = match[1]
    print(f"Verse {verse_number}: {lyrics}")

