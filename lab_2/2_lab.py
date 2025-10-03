import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Генерация данных
n = 500  # число строк (>400)
x1 = np.linspace(0.1, 10, n)   # начинаем с 0.1, чтобы избежать деления на ноль
x2 = np.linspace(0.1, 5, n)

# DataFrame
data = pd.DataFrame({
    "X1": x1,
    "X2": x2,
})

# Формула по варианту: Y = 3*X1 / (1 - exp(-X2))
data["Y"] = 3 * data["X1"] / (1 - np.exp(-data["X2"]))

# Сохраняем в CSV
data.to_csv("lab2_data.csv", index=False)
print("Файл lab2_data.csv создан!")

# 2. Построение графиков
# y(x1) при фиксированном x2
const_x2 = 2.5
y_x1 = 3 * x1 / (1 - np.exp(-const_x2))

plt.figure(figsize=(6,4))
plt.plot(x1, y_x1, 'r-', label=f"Y(X1), X2={const_x2}")
plt.scatter(x1, y_x1, s=10, color='blue')
plt.xlabel("X1")
plt.ylabel("Y")
plt.title("График Y(X1) при X2=const")
plt.legend()
plt.grid(True)
plt.show()

# y(x2) при фиксированном x1
const_x1 = 5
y_x2 = 3 * const_x1 / (1 - np.exp(-x2))

plt.figure(figsize=(6,4))
plt.plot(x2, y_x2, 'g-', label=f"Y(X2), X1={const_x1}")
plt.scatter(x2, y_x2, s=10, color='orange')
plt.xlabel("X2")
plt.ylabel("Y")
plt.title("График Y(X2) при X1=const")
plt.legend()
plt.grid(True)
plt.show()

# 3. Статистика по данным
stats = data.agg(["mean", "min", "max"])
print("Статистика по данным:")
print(stats)

# 4. Отбор строк: X1 < mean(X1) или X2 < mean(X2)
filtered = data[(data["X1"] < data["X1"].mean()) | (data["X2"] < data["X2"].mean())]
filtered.to_csv("lab2_filtered.csv", index=False)
print("Файл lab2_filtered.csv сохранен!")

# 5. 3D график функции
X1, X2 = np.meshgrid(x1, x2)
Y = 3 * X1 / (1 - np.exp(-X2))

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X1, X2, Y, cmap="viridis")
ax.set_xlabel("X1")
ax.set_ylabel("X2")
ax.set_zlabel("Y")
ax.set_title("3D график Y(X1, X2)")
plt.show()