# This is a dictionary on car functions. 
cars = {
    "press_unlock_button": "door unlocks",
    "pull_door_handle": "inner light comes on",
    "turns_ignition": "car starts",
    "engages_reverse_gear": "car moves back",
    "applies_break": "car slows down",
    "engages_forward gear": "car moves forward",
    "continue_engaging_forward_gear": "car accelerates",
    "steps_on_break": "car decelearates and stops",
    "steps_out_close_door": "inner light comes on and off",
    "press_lock_button": "car beeps two times, door locks", 

}
print(" ") # line 14 - 23 allows for expression. 
print(cars)
print(f"\n")
print(cars.keys())
print(f"\n")
print(cars.values())
print(f"\n")
print(type(cars))
print(" ")
print(len(cars))
for k, v in cars.items():
    print(f"\nk: {k}")
    print(f"v: {v}")
