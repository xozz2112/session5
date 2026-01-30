prompt = "what is you name? "
name = input(prompt)
print("nice to meet you,", name)
#if name == "bob":
#    print("FU bob")
#else:
#    print("nice to meet you,", name)

prompt2 = "how old are you, " + name + "? "
age = input(prompt2)
# convert to int
age = int(age)
print("you were born in,", 2025 - age)
