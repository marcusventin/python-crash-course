languages = ["ruby", "python", "css", "javascript"]

# Accessing elements
print("Accessing elements:")
print(languages)
print(languages[2].title())
print(languages[-1].title())

# Adding elements
languages.append("sql")
languages.insert(3, "c sharp")

# Removing elements
del languages[4]
print(f"\n{languages}")

languages.pop(2)
print(f"\n{languages}")

languages.remove("c sharp")
print(f"\n{languages}")

# Organising elements
print(f"\nUsing .reverse():")
print(languages)
languages.reverse()
print(languages)
languages.reverse()

print(f"\nUsing sorted():")
print(languages)
print(sorted(languages))
print(languages)

print(f"\nUsing .sort():")
languages.sort()
print(languages)

print(f"\nUsing len():")
print(len(languages))