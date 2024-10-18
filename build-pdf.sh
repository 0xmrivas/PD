#!/bin/bash

# Construir la programación y generar el PDF

# Reemplazar los archivos modX.md en PD.md
python scripts/replace-mods-pd.py
cd mkdocs-pd
mkdocs build

# Borrar la carpeta 'site' completa
rm -rf site

cd ..

# Construir el resumen y generar el PDF

# Extraer la información de los archivos modX.md en resumen.md
python scripts/extract-mods-resumen.py

cd mkdocs-resumen
mkdocs build

# Borrar la carpeta 'site' completa
rm -rf site