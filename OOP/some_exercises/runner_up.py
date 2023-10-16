# print the runner-up score

n = int(input())
int_lst = list(map(int, input().split()))

best_score = max(int_lst)
runner_up_lst = []

for score in int_lst:
    if score != best_score:
        runner_up_lst.append(score)

print(max(runner_up_lst))
