import numpy as np
import pulp as pl

# Створення моделі оптимізації
model = pl.LpProblem("Drinks_Optimization", pl.LpMaximize)

# Визначення змінних рішення
A = pl.LpVariable("Lemonade", lowBound=0, cat="Integer")
B = pl.LpVariable("Fruit_Juice", 0, cat="Integer")

# Додавання обмежень до моделі
model += A + B

# Обмеження на використання води
model += 2 * A + B <= 100  

# Обмеження на використання цукру
model += A <= 50  

# Обмеження на використання лимонного соку
model += A <= 30  

# Обмеження на використання фруктового пюре
model += 2 * B <= 40  

# Розв'язання моделі
model.solve()

# Виведення результатів
print("Lemonade:", pl.value(A))
print("Fruit_Juice:", pl.value(B))
print("State:", pl.LpStatus[model.status])
