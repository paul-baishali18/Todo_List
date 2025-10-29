
first_variable = "This is first"

second_variable = "This is second"

third_variable = first_variable
first_variable = second_variable
second_variable = third_variable

print(first_variable)
print(second_variable)


# without third variable

first_variable , second_variable = second_variable , first_variable
