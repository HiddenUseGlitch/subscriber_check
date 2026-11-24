following = input().split()
followers = input().split()
new_list = []

for i in following:
    if i not in followers:
        new_list.append(i)

print(new_list)