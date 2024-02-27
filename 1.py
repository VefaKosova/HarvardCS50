print("hello,", 1)

name = input("What's your name? ").strip().title()

# Remove whitespace from str
name= name.strip()

# Capitalize user's name
name = name.capitalize()
name = name.title()
name = name.strip().title()

# Seperating and Asigning 
first, last = name.split(" ")

print(f"hello, {name}")
print(f"hello, {first}")