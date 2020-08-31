n = int(input())
f = {'Tetrahedron': 4, 'Cube': 6, 'Octahedron': 8, 'Dodecahedron': 12, 'Icosahedron': 20}
s = 0
for i in range(n):
    cad = input()
    s += f[cad]
print(s)
