#!/bin/bash
# Construir la programación y generar el PDF
# Reemplazar los archivos modX.md en PD.md
cd mkdocs-pd
mkdocs build
# Borrar la carpeta 'site' completa
rm -rf site
cd ..
