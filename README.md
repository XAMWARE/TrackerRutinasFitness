# 🏋️ Fitness Tracker GM

Aplicación de consola para registrar y gestionar rutinas de ejercicio,
construida en Python con persistencia en SQLite.

## 🚀 Funcionalidades
- Agregar rutinas con múltiples ejercicios
- Calcular calorías quemadas por sesión
- Marcar rutinas como completadas
- Estadísticas semanales
- Eliminar rutinas

## 🛠️ Tecnologías
- Python 3.11+
- SQLite3 (base de datos local)
- Tabulate (formato de tablas)

## ▶️ Cómo correrlo

# 1. Clona el repositorio
git clone https://github.com/XAMWARE/TrackerRutinasFitness.git
cd TrackerRutinasFitness

# 2. Instala dependencias
pip install tabulate

# 3. Ejecuta
python main.py

## 📁 Estructura del proyecto
fitness-tracker/
├── main.py       # Menú principal
├── gestor.py     # Lógica de negocio
├── database.py   # Capa de datos SQLite
├── modelos.py    # Clases: Ejercicio, Rutina, Persona
└── README.md

## 👤 Autor
Matthias — github.com/XAMWARE
