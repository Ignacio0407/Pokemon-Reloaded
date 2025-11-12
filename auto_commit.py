import time
import subprocess

# Carpetas que quieres vigilar
WATCHED_DIRS = [
    "data/equipos",
    "data/partidas",
    "data/capturas",
    "data/char_custom"
]

# Intervalo en minutos
INTERVAL = 10   # cámbialo a lo que quieras, por ejemplo 10 minutos

def commit_and_push():
    try:
        subprocess.run(["git", "add"] + WATCHED_DIRS, check=True)
        # Si no hay cambios, git commit fallará → lo controlamos con try/except
        subprocess.run(["git", "commit", "-m", "Auto-commit: cambios en partidas"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Cambios subidos a GitHub.")
    except subprocess.CalledProcessError:
        print("No hay cambios nuevos.")

if __name__ == "__main__":
    print(f"Ejecutando auto-commit cada {INTERVAL} minutos...")
    while True:
        commit_and_push()
        time.sleep(INTERVAL * 60)
