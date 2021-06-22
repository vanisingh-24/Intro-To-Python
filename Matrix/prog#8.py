## Given a String Matrix, perform column-wise concatenation of strings, handling variable lists lengths.

test_list = [["Gfg", "good"], ["is", "for"], ["Best"]]

print(test_list)

res = []
N = 0
while N != len(test_list):
    temp = ''
    for i in test_list:
        try: temp = temp + i[N]
        except IndexError: pass
    res.append(temp)
    N = N+1

res = [el for el in res if el]

print("List after column Concatenation : " + str(res))



