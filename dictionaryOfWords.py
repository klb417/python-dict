"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["ninja turtles"] = "heroes in a half shell"
word_definitions["ghostbusters"] = "who ya gonna call"
word_definitions["power rangers"] = "it's mighty morphin' time"
word_definitions["gi joe"] = "knowing is half the battle"
word_definitions["he-man"] = "i have the power"
"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["power rangers"])
print(word_definitions["he-man"])


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for (key, value) in word_definitions.items():
    print(f"The definition of the {key} is {value}")
