# 1
NAME_FILE = "name.txt"
add_name = str(input("Enter your name: "))
out_file = open(NAME_FILE, 'w')
print("", add_name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", 'r')
read_name = in_file.read()
in_file.close()
print("Your name is", end=read_name)

# 3
NUMBER_FILE = "numbers.txt"
out_file = open(NUMBER_FILE, 'w')
print("17\n42\n400", file=out_file)
out_file.close()

in_file = open("numbers.txt", 'r')
total = int(in_file.readline()) + int(in_file.readline())
in_file.close()
print(total)

# 4
total = 0
in_file = open("numbers.txt", 'r')
for number in in_file:
    number = int(number)
    total += number
in_file.close()
print(total)
