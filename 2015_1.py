with open("2015_1_input.txt") as file:
    sequence = file.read()

location = 0
basement_seen = False

for i, char in enumerate(sequence):
    if char == "(":
        location +=1
    else:
        location -=1
    if location == -1 and not basement_seen:
        basement_seen = True
        print(f'Index where basement is first seen is {i + 1}')

print(f'Final location for Santa is {location}')