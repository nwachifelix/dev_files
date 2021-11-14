# List of early birds that attended the live coding session last night.
attendancelist = []               # first I created an empty list named attendancelist
a = input("First students: ")
attendancelist.append(a)          # Next, started adding students in the list using the .append() method

a = input("Second student: ")
attendancelist.append(a)

a = input("Third student: ")
attendancelist.append(a)
# print(attendancelist)

a = input("Fourth student: ")
attendancelist.append(a)

a = input("Fifth student: ")
attendancelist.append(a)

a = input("Sixth student: ")
attendancelist.append(a)

a = input("Seventh student: ")
attendancelist.append(a)
# At line 26 started adding late comers.
attendancelist.insert(7, "zarah") 
attendancelist.insert(8, "Tosin")
attendancelist.insert(9, "chioma")
print(attendancelist)