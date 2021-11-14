# First, making a list of three people and inviting them to a dinner at my residence. 
invite = ["arinze", "vee", "josiah" ]
print(f"\n\tHi {invite[0].title()}, I'm inviting you to a dinner at my residence tonight by 7pm.\n\tHi {invite[1].title()}, I'm inviting you to a dinner at my residence tonight by 7pm.\n\tHi {invite[2].title()}, I'm inviting you to a dinner at my residence tonight by 7pm. ")
popped_invite = invite.pop(2)
print(invite)
# A slight change to the list after one of the guests will not be attending. 
print(f"Unfortunately, {popped_invite.title()} will not be joining us tonight. He has business meeting to attend first thing tomorrow morning. ")
invite.append("mosh")    # Replace a guest and send a fresh invite to the current list. 
print(invite)
print(f"\n\tHi {invite[0].title()}, I'm inviting you to a dinner at my residence tonight by 7pm.\n\tHi {invite[1].title()}, I'm inviting you to a dinner at my residence tonight by 7pm.\n\tHi {invite[2].title()}, I'm inviting you to a dinner at my residence tonight by 7pm. ")
# # Adding 3 more friends to the dinner tonight using insert() and append() methods. 
invite.insert(0, "vienivre")
invite.insert(3, "chima")
invite.append("tosin")
print(invite)
print(f"\n\tHi {invite[0].title()}, I'm inviting you to a dinner at my residence tonight by 7pm.\n\tHi {invite[1].title()}, I'm inviting you to a dinner at my residence tonight by 7pm.\n\tHi {invite[2].title()}, I'm inviting you to a dinner at my residence tonight by 7pm.\n\tHi {invite[3].title()}, I'm inviting you to a dinner at my residence tonight by 7pm.\n\tHi {invite[4].title()}, I'm inviting you to a dinner at my residence tonight by 7pm.\n\tHi {invite[5].title()}, I'm inviting you to a dinner at my residence tonight by 7pm. ")
# Change of plans. Using pop() method to remove guests one at a time from the list and sending each a personal message. 
popped_invite = invite.pop()
print(f"I'm sorry {popped_invite.title()}, the dinner will not hold again. ")
popped_invite = invite.pop()
print(f"I'm sorry {popped_invite.title()}, dinner is cancelled. ")
popped_invite = invite.pop()
print(f"I'm sorry {popped_invite.title()}, the dinner is cancelled. ")
popped_invite = invite.pop()
print(f"I'm sorry {popped_invite.title()}, the dinner will not go on as planned. ")
print(f"{invite[0].title()}: The dinner will still go on as planned. " )
print(f"{invite[1].title()}: The dinner will still go on as planned. ")
# Finally, delette the remaining items of the list and print an empty list. 
del invite[0]
del invite[-1]
print(invite)