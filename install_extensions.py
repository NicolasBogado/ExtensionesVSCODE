import subprocess
import os

def install_extensions(requirements_file):
    if not os.path.isfile(requirements_file):
        print(f"El archivo {requirements_file} no fue encontrado.")
        return

    try:
        with open(requirements_file, 'r') as file:
            extensions = file.readlines()
        
        extensions = [ext.strip() for ext in extensions if ext.strip()]

        for extension in extensions:
            print(f"Instalando extensión: {extension}")
            try:
                result = subprocess.run(['code', '--install-extension', extension], capture_output=True, text=True, shell=True)
                if result.returncode == 0:
                    print(f"Extensión {extension} instalada con éxito.")
                else:
                    print(f"Error instalando la extensión {extension}:\n{result.stderr}")
            except FileNotFoundError:
                print(f"El comando 'code' no se encontró. Asegúrate de que VSCode está instalado y el comando 'code' está en el PATH.")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    requirements_file = 'requerimientos_vscode.txt'
    print(f"Buscando el archivo {requirements_file} en el directorio {os.getcwd()}")
    install_extensions(requirements_file)
