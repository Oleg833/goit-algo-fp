# Функція для обчислення максимальної вартості
def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0

    if wt[n - 1] > W:
        return knapSack(W, wt, val, n - 1)

    else:
        return max(
            val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
            knapSack(W, wt, val, n - 1),
        )


value = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50
n = len(value)
print(knapSack(capacity, weight, value, n))  # 220
