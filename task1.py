import numpy as np

# Створення двовимірного масиву 3x3 з випадкових цілих чисел від 1 до 100
array = np.random.randint(1, 101, size=(3, 3))
print("Масив:\n", array)

# Обчислення суми всіх елементів масиву
total_sum = np.sum(array)
print("Сума всіх елементів:", total_sum)

# Максимальне та мінімальне значення, а також їхні індекси
max_value = np.max(array)
min_value = np.min(array)

max_index = np.unravel_index(np.argmax(array), array.shape)
min_index = np.unravel_index(np.argmin(array), array.shape)

print("Максимальне значення:", max_value, "Індекс:", max_index)
print("Мінімальне значення:", min_value, "Індекс:", min_index)

# Сортування масиву по кожному рядку
sorted_array = np.sort(array, axis=1)
print("Відсортований масив по рядках:\n", sorted_array)