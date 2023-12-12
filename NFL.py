week0=[[1,5],[2,6],[3,7],[4,8]]
week1=[[3,4],[5,6],[7,8]]
week2=[[1,2],[5,7],[6,8]]
week3=[[1,3],[2,4]]
week4=[[1,8],[2,7],[3,6],[4,5]]
game=[]
game.append((week0))
game.append((week1))
game.append((week2))
game.append((week3))
game.append((week4))
target_list=[]
def backtrack(list1,i):
    if len(list1)==5:
        tuple1=tuple(list1)
        target_list.append(tuple1)
        return
    else:
        for x in game[i]:
            for y in x:
                if y in list1:
                    continue
                list1.append(y)
                backtrack(list1,i+1)
                list1.pop(-1)
backtrack([],0)
with open(r"C:\Users\黄枢炜\Desktop\output.txt",'w') as file1:
    print(target_list,file=file1)