#codechef problem : Smart Phone   Code: ZCQ14003
N = int(input("Enter numbers of potential customers: "))
budgets = list()
values = list()

for _ in range(N):
    budgets.append(int(input("Enter bugets")))

budgets.sort()
for i in range(N):
    values.append(budgets[i] * (N-i))

values.sort()
print(values[N-1])
