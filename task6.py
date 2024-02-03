def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item_name, item_info in sorted_items:
        if total_cost + item_info["cost"] <= budget:
            selected_items.append(item_name)
            total_cost += item_info["cost"]
            total_calories += item_info["calories"]

    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories,
    }


def dynamic_programming(items, budget):
    dp_table = [[0] * (budget + 1) for _ in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        item_name = list(items.keys())[i - 1]
        cost = items[item_name]["cost"]
        calories = items[item_name]["calories"]

        for j in range(budget + 1):
            if cost > j:
                dp_table[i][j] = dp_table[i - 1][j]
            else:
                dp_table[i][j] = max(
                    dp_table[i - 1][j], dp_table[i - 1][j - cost] + calories
                )

    selected_items = []
    i, j = len(items), budget
    while i > 0 and j > 0:
        item_name = list(items.keys())[i - 1]
        cost = items[item_name]["cost"]
        calories = items[item_name]["calories"]

        if dp_table[i][j] != dp_table[i - 1][j]:
            selected_items.append(item_name)
            j -= cost

        i -= 1

    selected_items.reverse()

    return {
        "selected_items": selected_items,
        "total_cost": sum(items[item]["cost"] for item in selected_items),
        "total_calories": dp_table[len(items)][budget],
    }


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("Greedy Algorithm Result:")
    print(greedy_result)

    print("\nDynamic Programming Result:")
    print(dp_result)


if __name__ == "__main__":
    main()
