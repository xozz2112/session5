prompt = "what is you name? "
name = input(prompt)
print("nice to meet you,", name)

try:
    prompt2 = "how old are you, " + name + "? "
    age = input(prompt2)
    # convert to int
    age = int(age)
    print("you were born in,", 2025 - age)
    # primt("nice knowing you")
    a = 7 / 6
except ValueError:
    print("sorry, ", name, "but tbat is not a number")
except NameError:
    print("sorry that is not a valid name for print")
except:
    print("all other exceptions go here!")
else:
    print("thank you for playing fair and square")
finally:
    print("this is always at the end no matter what")

