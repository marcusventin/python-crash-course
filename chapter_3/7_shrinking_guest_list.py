guest_list = ["teddy roosevelt", "santa claus", "mr rogers"]
print(guest_list[1])

guest_list[1] = "mrs claus"

print("We have found a bigger table")

guest_list.insert(0, "Granny Weatherwax")
guest_list.insert(1, "Sybil Vimes")
guest_list.append("Captain Carrot")

print(f"{guest_list[0].title()}, you are cordially invited...")
print(f"{guest_list[1].title()}, you are coridally invited...")
print(f"{guest_list[2].title()}, you are cordially invited...")
print(f"{guest_list[3].title()}, you are cordially invited...")
print(f"{guest_list[4].title()}, you are cordially invited...")
print(f"{guest_list[5].title()}, you are cordially invited...")

print("Oh no! Due to pandemic restrictions we can only host two guests.")

print(f"{guest_list.pop(2).title()}, you are cordially uninvited...")
print(f"{guest_list.pop(2).title()}, you are cordially uninvited...")
print(f"{guest_list.pop().title()}, you are cordially uninvited...")
print(f"{guest_list.pop(1).title()}, you are cordially uninvited...")

print(f"{guest_list[0].title()}, you are still cordially invited...")
print(f"{guest_list[1].title()}, you are still cordially invited...")

del guest_list[1]
del guest_list[0]

print(guest_list)