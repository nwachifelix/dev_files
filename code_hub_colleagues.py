# A simple code on list and how to access individual items in a list. The f farmat, title(), and \n, \t were practiced on.



names = ['arinze', 'mosh', 'chima', 'vievie', 'bravestone', 'tochukwu']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[-3].title())
print(names[-2].title())
print(names[-1].title())

greetings = f'\n\tHow are you today {names[0].title()}?\n\tHow are you today {names[1].title()}?\n\tHow are you today {names[2].title()}?\n\tHow are you today {names[-3].title()}?\n\tHow are you today {names[-2].title()}?\n\tHow are you today {names[-1].title()}?'
print(greetings)
