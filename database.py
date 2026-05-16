import sqlite3

DB_NAME = "fitness.db"  # el archivo se crea automáticamente

def conectar():
    """Retorna una conexión a la base de datos."""
    return sqlite3.connect(DB_NAME)


def crear_tablas():
    """Crea todas las tablas si no existen."""
    conn = conectar()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS personas (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre  TEXT NOT NULL,
            edad    INTEGER,
            peso    REAL,
            altura  REAL
        );

        CREATE TABLE IF NOT EXISTS rutinas (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha       TEXT NOT NULL,
            duracion    INTEGER,
            completada  INTEGER DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS ejercicios (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            rutina_id   INTEGER NOT NULL,
            nombre      TEXT NOT NULL,
            series      INTEGER,
            repeticiones INTEGER,
            calorias    REAL,
            peso_kg     REAL DEFAULT 0,
            FOREIGN KEY (rutina_id) REFERENCES rutinas(id)
        );
    """)

    conn.commit()
    conn.close()
    print("✅ Base de datos lista.")


# ─── PERSONAS ────────────────────────────────────────────

def insertar_persona(persona):
    """Guarda un objeto Persona en la base de datos."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO personas (nombre, edad, peso, altura)
        VALUES (?, ?, ?, ?)
    """, (persona.nombre, persona.edad, persona.peso, persona.altura))
    conn.commit()
    conn.close()


def obtener_persona():
    """Retorna la primera persona registrada (tu perfil)."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personas LIMIT 1")
    fila = cursor.fetchone()
    conn.close()
    return fila  # (id, nombre, edad, peso, altura)


# ─── RUTINAS ─────────────────────────────────────────────

def insertar_rutina(rutina):
    """Guarda una Rutina y todos sus ejercicios. Retorna el ID generado."""
    conn = conectar()
    cursor = conn.cursor()

    # 1. Insertar la rutina
    cursor.execute("""
        INSERT INTO rutinas (fecha, duracion, completada)
        VALUES (?, ?, 0)
    """, (rutina.fecha, rutina.tiempo))

    rutina_id = cursor.lastrowid  # ID que SQLite le asignó automáticamente

    # 2. Insertar cada ejercicio vinculado a esa rutina
    for e in rutina.ejercicios:
        cursor.execute("""
            INSERT INTO ejercicios (rutina_id, nombre, series, repeticiones, calorias, peso_kg)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (rutina_id, e.nombre, e.series, e.repeticiones, e.calorias, e.peso_kg))

    conn.commit()
    conn.close()
    return rutina_id


def obtener_rutinas():
    """Retorna todas las rutinas con sus ejercicios."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rutinas ORDER BY fecha DESC")
    rutinas = cursor.fetchall()
    conn.close()
    return rutinas  # lista de tuplas (id, fecha, duracion, completada)


def completar_rutina(rutina_id):
    """Marca una rutina como completada por su ID."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE rutinas SET completada = 1 WHERE id = ?
    """, (rutina_id,))
    conn.commit()
    conn.close()


def obtener_ejercicios_de_rutina(rutina_id):
    """Retorna todos los ejercicios de una rutina específica."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM ejercicios WHERE rutina_id = ?
    """, (rutina_id,))
    ejercicios = cursor.fetchall()
    conn.close()
    return ejercicios


# ─── ESTADÍSTICAS ────────────────────────────────────────

def total_calorias_semana():
    """Suma las calorías de todos los ejercicios de esta semana."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COALESCE(SUM(e.calorias), 0)
        FROM ejercicios e
        JOIN rutinas r ON e.rutina_id = r.id
        WHERE r.fecha >= date('now', '-7 days')
    """)
    resultado = cursor.fetchone()[0]
    conn.close()
    return resultado
