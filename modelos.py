class Ejercicio:
    def __init__(self, nombre, series, repeticiones, calorias, peso_kg=0):
        self.nombre = nombre
        self.series = series
        self.repeticiones = repeticiones
        self.calorias = calorias
        self.peso_kg = peso_kg
    def volumen(self):              
        return self.series * self.repeticiones * self.peso_kg

    def __str__(self):              
        return f"{self.nombre} | {self.series}x{self.repeticiones} | {self.calorias} kcal"

class Persona:
    def __init__(self, nombre_completo, edad, peso, altura):
        self.nombre = nombre_completo
        self.edad = edad
        self.peso = peso
        self.altura = altura
    def imc(self):
        return round(self.peso / (self.altura ** 2), 2) 
    def categoria_imc(self):
        imc = self.imc()
        if imc < 18.5: return "Bajo peso"
        elif imc < 25: return "Normal"
        elif imc < 30: return "Sobrepeso"
        else: return "Obesidad"

class Rutina:
    def __init__(self, fecha,duracion, lista_ejercicios):
        self.fecha = fecha
        self.tiempo = duracion
        self.ejercicios = lista_ejercicios

    def total_series(self):
        return sum(e.series for e in self.ejercicios)

    def total_calorias(self):
        return sum(e.calorias for e in self.ejercicios)

    def __str__(self):
        return f"Rutina {self.fecha} | {len(self.ejercicios)} ejercicios | {self.total_calorias()} kcal"
