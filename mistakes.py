s1 = input()
s2 = input()

mistakes = [1 if s1[i] != s2[i] else 0 for i in range(len(s1))]
print(sum(mistakes))