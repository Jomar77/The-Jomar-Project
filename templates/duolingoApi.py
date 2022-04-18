
import duolingo as dl
import json

lingo = dl.Duolingo('MojNac','7M36veGfShEWkQh')
json_file = json.dumps(lingo.get_streak_info(), indent=4)
with open("duo.json", "w") as outfile:
    outfile.write(json_file)
