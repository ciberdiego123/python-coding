from bisect import bisect_right

def create_index_directionary(base):
    d = dict()
    for i in range(len(base)):
        if base[i] not in d:
            d[base[i]] = [i]
        else:
            d[base[i]].append(i)
    return d


def longest_spell(d, word):
    spell, k = '', -1
    for i in range(len(word)):
        if word[i] in d:
            limit = bisect_right(d[word[i]], k)
            if limit == len(d[word[i]]):
                break
            mini = d[word[i]][limit]
            if mini > k:
                k = mini
                spell += word[i]
            else:
                break
        else:
            break
    return spell if len(spell) > 0 else 'IMPOSSIBLE'


s = input()
n = int(input())
d = create_index_directionary(s)
for i in range(n):
    l = input()
    print(longest_spell(d, l))


