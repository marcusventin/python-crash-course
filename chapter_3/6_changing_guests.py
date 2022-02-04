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
