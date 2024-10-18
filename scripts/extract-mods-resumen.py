import re
import os

# Ruta del archivo principal
main_file = 'src/resumen.md'

# Leer el contenido del archivo principal
with open(main_file, 'r', encoding='utf-8') as file:
    content = file.read()

# Inicializar una lista para almacenar el contenido de los archivos modX.md
mod_contents = []

# Simular la existencia de archivos modX.md (ajusta según tu estructura real)
mod_files = [f'src/mod{i}.md' for i in range(1, 7)]  # Cambia el rango según tus archivos

for mod_filename in sorted(mod_files):
    if os.path.exists(mod_filename):
        with open(mod_filename, 'r', encoding='utf-8') as mod_file:
            mod_content = mod_file.read()
            # Eliminar la sección ## Contenidos
            mod_content = re.sub(r'##\s*Contenidos\n.*?(?=### |\Z)', '', mod_content, flags=re.DOTALL)
            # Eliminar la sección ### Contenidos del currículo hasta ### Selección y secuencia de contenidos
            mod_content = re.sub(r'###\s*Contenidos del currículo.*?(?=### Selección y secuencia de contenidos|\Z)', '', mod_content, flags=re.DOTALL)
            # Convertir ### Selección y secuencia de contenidos a ## Selección y secuencia de contenidos
            mod_content = re.sub(r'###\s*Selección y secuencia de contenidos', '## Selección y secuencia de contenidos', mod_content)
            # Eliminar secciones ### Tratamiento de temas transversales y ### Interdisciplinaridad
            mod_content = re.sub(r'###\s*Tratamiento de temas transversales.*?(?=### |\Z)', '', mod_content, flags=re.DOTALL)
            mod_content = re.sub(r'###\s*Interdisciplinaridad.*?(?=## |\Z)', '', mod_content, flags=re.DOTALL)
            # Eliminar ## Bibliografía y referencias y subsecciones
            mod_content = re.sub(r'##\s*Bibliografía y referencias.*', '', mod_content, flags=re.DOTALL)
            
            # Añadir el contenido procesado a la lista
            mod_contents.append(mod_content)

# Concatenar el contenido de los módulos al inicio del contenido actual
final_content = '\n'.join(mod_contents) + '\n' + content

# Guardar el nuevo contenido en un nuevo archivo o sobrescribir el existente
with open('mkdocs-resumen/docs/resumen.md', 'w', encoding='utf-8') as file:
    file.write(final_content)

print("Extracción completada. El archivo resultante es resumen.md.")