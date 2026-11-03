# Samuel Martinez NC 0096

import matplotlib.pyplot as plt
import numpy as np

materias = ['Mate', 'Física', 'VA', 'ML', 'Química']
calificaciones = [85, 90, 78, 95, 88]

plt.pie(calificaciones, labels=materias, autopct='%1.1f%%')
plt.title("Calificaciones por Materia - 0096")
plt.show()
print("Samuel Martinez NC 0096")
