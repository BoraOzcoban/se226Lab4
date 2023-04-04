dict = {}
for x in range(1, 31):
    dict[x] = (x - 1) * x
print(dict)

for k, v in dict.items():
    print(f"{k}: {v}")

sum_ = 0
for v in dict.values():
    sum_ += v
print("Sum:", sum_)

user_input = input("Please choose a number: ")
if user_input.isdigit() and int(user_input) in dict:
    del dict[int(user_input)]
print("New dictionary:", dict)