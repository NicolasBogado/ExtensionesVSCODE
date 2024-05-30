# ExtensionesVSCODE
Script de python para instalar las extensiones que consideres necesarias, para trabajar con el VSCODE.
Cuando comenzamos a desarrollar necesitamos extensiones que nos faciliten el trabajo, lo tedioso es que se deben instalar de a una. Por lo que diseñe el script para instalar todas de una sola vez, solo sigue los pasos y ejecuta el script.

## Guía de Configuración de extensiones de Visual Studio Code
¡Bienvenido! Esta guía te ayudará a configurar las extensiones de VSCode correctamente, para que puedas empezar a utilizarlo de manera eficiente. Asegúrate de tener instalado VSCode en tu computadora y que el PATH esté correctamente configurado antes de comenzar.

## Paso 1: Instalación de Visual Studio Code
Descarga e instala Visual Studio Code desde la página oficial de descargas.
Sigue las instrucciones del instalador para completar la instalación.

## Paso 2: Configuración del PATH de Visual Studio Code
Es importante tener el PATH de Visual Studio Code configurado correctamente para acceder a él desde la línea de comandos.
Abre Visual Studio Code.
Abre la paleta de comandos presionando Ctrl+Shift+P (Windows/Linux) o Cmd+Shift+P (Mac).
Escribe "shell command" y selecciona la opción "Shell Command: Install 'code' command in PATH".
¡Listo! Ahora puedes abrir VSCode desde la línea de comandos escribiendo code.

## Paso 3: Instalación de Extensiones
Las extensiones son herramientas adicionales que amplían la funcionalidad de Visual Studio Code. Asegúrate de utilizar los identificadores correctos al instalar las extensiones.
Crea un archivo de texto llamado requerimientos_vscode.txt en tu directorio de trabajo.
Lista las extensiones que deseas instalar, cada una en una línea separada, utilizando el formato publisher.extensionName. 
Por ejemplo:
arduino
Copiar código
formulahendry.auto-close-tag
ms-python.python
dbaeumer.vscode-eslint
ritwickdey.live-sass
Guarda el archivo y asegúrate de que esté en el mismo directorio que tu script de instalación.

## Paso 4: Ejecutar el Script de Instalación
Ahora que tienes tu lista de extensiones en el archivo requerimientos_vscode.txt, puedes ejecutar el script de instalación para instalarlas todas de una vez.
Abre la línea de comandos.
Navega hasta el directorio donde tienes tu script de instalación y el archivo requerimientos_vscode.txt.
Ejecuta el script de instalación utilizando el siguiente comando:
bash
Copiar código
python install_extensions.py

## Paso 5: ¡Disfruta de Visual Studio Code!
¡Felicidades! Has configurado correctamente Visual Studio Code y has instalado las extensiones que necesitas. Ahora puedes empezar a utilizar VSCode para desarrollar tus proyectos de manera eficiente y productiva. Si necesitas ayuda adicional, no dudes en consultar la documentación oficial de VSCode o la comunidad en línea. ¡Feliz codificación!

## Captura pantalla
![Captura de pantalla 2024-05-30 115040](https://github.com/NicolasBogado/ExtensionesVSCODE/assets/112599449/6b2c95a7-9d6e-44b6-a417-57c67cec93ad)

