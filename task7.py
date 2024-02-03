import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_simulations):
    results = {i: 0 for i in range(2, 13)}

    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total_sum = dice1 + dice2
        results[total_sum] += 1

    probabilities = {
        key: value / num_simulations * 100 for key, value in results.items()
    }
    return probabilities


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probabilities_values = list(probabilities.values())

    plt.bar(sums, probabilities_values, color="blue", alpha=0.7)

    # Додавання точок на вершинах
    for sum_val, prob_val in zip(sums, probabilities_values):
        plt.scatter(sum_val, prob_val, color="red", zorder=5)

    # З'єднання точок лініями
    plt.plot(
        sums,
        probabilities_values,
        color="green",
        linestyle="dashed",
        linewidth=2,
        markersize=8,
        marker="o",
        markerfacecolor="yellow",
    )

    plt.xlabel("Сума")
    plt.ylabel("Ймовірність (%)")
    plt.title("Ймовірність сум при киданні двох кубиків (Метод Монте-Карло)")
    plt.show()


# Кількість симуляцій
num_simulations = 100000

# Виконання симуляції та отримання ймовірностей
probabilities = simulate_dice_rolls(num_simulations)

# Виведення результатів
for key, value in probabilities.items():
    print(f"Сума {key}: {value:.2f}%")

# Побудова графіку
plot_probabilities(probabilities)
