from NFL import target_list
from win_probablity import p
max_win=0
best=()
for x in target_list:
    c=1
    i=0
    for y in x:
        c*=p[i][y]
        i+=1
    if c>max_win:
        max_win=c
        best=x
print(max_win)
print(best)
