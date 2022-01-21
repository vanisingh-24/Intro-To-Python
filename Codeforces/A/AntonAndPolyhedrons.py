'''
https://codeforces.com/problemset/problem/785/A
Solution: Keep a dictionary for polyhedron name to the total sides it has. Run through the input list of polyhedrons 
and sum their sides using this dictionary. 
'''

n = int(input())
polyhedrons = {
    'Tetrahedron': 4,
    'Cube': 6,
    'Octahedron': 8,
    'Dodecahedron': 12,
    'Icosahedron': 20
}
faces = 0

for i in range(n):
  face = input()
  faces += polyhedrons[face]
print(faces)
