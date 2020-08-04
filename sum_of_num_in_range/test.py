def add_num_in_range(input):
    global counter
    if input <= 99 and input > 0:
        counter += input

counter = 0
user_input = int(raw_input("Enter number (0 to stop): "))

while user_input != 0:
    add_num_in_range(user_input)
    user_input = int(raw_input("Enter number (0 to stop): "))
print counter
