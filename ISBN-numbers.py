import re
string = "Game of thrones (2011), House of dragons (2022), [Verse 1] I can't hide myself I don't expect you understand I just hope I can explain What it's like to be a man It's a lonely road, @DenmarkEddy, ISBN 123-5-678-90123-4, @TodoSabio, Breaking Bad (2005), @ElMayor, Why did the seagulls fly over the ocean? Because if they flew over the bay, Expanse S01E01: , 01-Jan-2023, #ABC123, 192.168.0.1, ISBN 153-5-678-90123-4, ISBN 163-5-678-90123-4, Stranger Things (2016),"

pattern = r"ISBN \d{3}-\d-\d{3}-\d{5}-\d"

result = re.findall(pattern, string)
print("The ISBN Number: ",result)
