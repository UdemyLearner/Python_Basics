programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary)

programming_dictionary["Loop"]="Doing Something again and again"

empty_dictionary={}
print(empty_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    print()
