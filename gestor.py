from datetime import date
from modelos import Ejercicio, Rutina
import database as db


# ─── AGREGAR ─────────────────────────────────────────────

def agregar_rutina():
    print("\n─── Nueva Rutina ───")
    fecha = str(date.today())
    
    try:
        duracion = int(input("Duración (minutos): "))
    except ValueError:
        print("❌ Ingresa un número válido.")
        return

    ejercicios = []
    while True:
        print(f"\nEjercicio #{len(ejercicios) + 1} (deja el nombre vacío para terminar)")
        nombre = input("Nombre del ejercicio: ").strip()
        if not nombre:
            break

        try:
            series      = int(input("Series: "))
            reps        = int(input("Repeticiones: "))
            calorias    = float(input("Calorías estimadas: "))
            peso_kg     = float(input("Peso usado en kg (0 si no aplica): "))
        except ValueError:
            print("❌ Valor inválido, ejercicio omitido.")
            continue

        ejercicios.append(Ejercicio(nombre, series, reps, calorias, peso_kg))

    if not ejercicios:
        print("❌ No agregaste ningún ejercicio, rutina cancelada.")
        return

    rutina = Rutina(fecha, duracion, ejercicios)
    rutina_id = db.insertar_rutina(rutina)
    print(f"\n✅ Rutina guardada con ID {rutina_id} — {len(ejercicios)} ejercicio(s) registrados.")


# ─── LISTAR ──────────────────────────────────────────────

def listar_rutinas():
    rutinas = db.obtener_rutinas()

    if not rutinas:
        print("\n📭 No hay rutinas registradas aún.")
        return

    print("\n─── Tus Rutinas ───")
    for r in rutinas:
        id_, fecha, duracion, completada = r
        estado = "✅ Completada" if completada else "⏳ Pendiente"
        ejercicios = db.obtener_ejercicios_de_rutina(id_)
        total_cal = sum(e[5] for e in ejercicios)  # índice 5 = calorias

        print(f"\n[{id_}] {fecha} | {duracion} min | {estado}")
        print(f"     Ejercicios: {len(ejercicios)} | Calorías: {total_cal} kcal")
        for e in ejercicios:
            print(f"     • {e[2]} — {e[3]}x{e[4]} | {e[5]} kcal | {e[6]} kg")


# ─── COMPLETAR ───────────────────────────────────────────

def completar_rutina():
    listar_rutinas()
    try:
        id_ = int(input("\nID de la rutina a completar: "))
        db.completar_rutina(id_)
        print("✅ Rutina marcada como completada.")
    except ValueError:
        print("❌ Ingresa un ID válido.")


# ─── ELIMINAR ────────────────────────────────────────────

def eliminar_rutina():
    listar_rutinas()
    try:
        id_ = int(input("\nID de la rutina a eliminar: "))
        confirmar = input(f"¿Seguro que quieres eliminar la rutina {id_}? (s/n): ")
        if confirmar.lower() == 's':
            db.eliminar_rutina(id_)
            print("🗑️ Rutina eliminada.")
        else:
            print("Cancelado.")
    except ValueError:
        print("❌ Ingresa un ID válido.")


# ─── ESTADÍSTICAS ────────────────────────────────────────

def mostrar_estadisticas():
    calorias = db.total_calorias_semana()
    print(f"\n📊 Calorías quemadas esta semana: {calorias} kcal")