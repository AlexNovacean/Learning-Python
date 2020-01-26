# Ask user for name

name = input('What is your name?: ')

# Ask user for their age

age = input('How old are you?: ')

# Ask user for their city

city = input('What city do you live in?: ')

# Ask user what they enjoy

love = input('What do you enjoy doing?: ')

# Create output text

base_string = 'Your name is {} and you are {} year old. You live in {} and you love {}.'
output = base_string.format(name, age, city, love)

# Print output to screen

print(output)
