import gestor
import database as db


def menu():
    db.crear_tablas()  # crea fitness.db si no existe

    while True:
        print("""
╔══════════════════════════════╗
║   🏋️  Fitness Tracker GM     ║
╠══════════════════════════════╣
║  1. Agregar rutina           ║
║  2. Ver rutinas              ║
║  3. Completar rutina         ║
║  4. Eliminar rutina          ║
║  5. Estadísticas             ║
║  6. Salir                    ║
╚══════════════════════════════╝
        """)

        try:
            op = int(input("   Elige una opción: "))
        except ValueError:
            print("❌ Ingresa un número del 1 al 6.")
            continue

        match op:
            case 1: gestor.agregar_rutina()
            case 2: gestor.listar_rutinas()
            case 3: gestor.completar_rutina()
            case 4: gestor.eliminar_rutina()
            case 5: gestor.mostrar_estadisticas()
            case 6:
                print("\n👋 ¡Hasta luego!")
                break
            case _:
                print("❌ Opción no válida, elige entre 1 y 6.")


if __name__ == "__main__":
    menu()