# Intro to dictionaries and some of the things we can do with it. 
felix = {"complexion": "dark", "height": "6.5inch", "level": "upper"}
print(felix)
print(felix["complexion"].title())
print(felix["height"].title())
print(felix["level"].title())
print(felix.keys())
print(felix.values())
print(type(felix))
felix["occupation"] = "cargo surveyor"
felix["post"] = "supervisor"
print(felix)
# Modify felix's post. 
felix["post"] = "base manager"
print(f"Felix has been promoted and his current post is {felix['post']}. ")
print(felix)
# Colleagues roadmap as pythonistas. 
road_maps = {
    "vee": "undecided",
    "felix": "webdev/data/sql",
    "augustinechima": "data/webdev/sql",
    "vienivre": "webdev",
    "stella": "data analysis/sql",
    }
# Looping through dictionaries. 
for key, value in road_maps.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
for name, roadmap in road_maps.items():
    print(f"\n{name.title()}'s roadmap is: {roadmap.title()}.")
