n = int(input())
inital_state = input()
correct_state = input()
total_Moves =0
for i in range(n):
    dis = abs(int(inital_state[i]) - int(correct_state[i]))
    total_Moves += min(dis, 10-dis)
print(total_Moves)