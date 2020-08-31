word = input()
word_list = list(word)
n = len(word_list)
first_lower = word_list[0].islower()
rest_upper = True
for i in range(1, n):
    if word_list[i].islower():
        rest_upper = False
        break
if first_lower and rest_upper:
    word_list[0] = word_list[0].upper()
    for i in range(1, n):
        word_list[i] = word_list[i].lower()
    word = "".join(word_list)
elif not first_lower and rest_upper:
    word = word.lower()
print(word)
