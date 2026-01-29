import os
import json

# Configuración
carpeta_img = 'img'
archivo_salida = 'datos_galeria.js'

# Las carpetas que vamos a escanear (tienen que existir dentro de img/)
categorias = ['techumbres', 'losas_pisos', 'ampliaciones', 'terminaciones', 'estructuras', 'gasfiteria', 'soldadura']

datos = {}

print("🔄 Escaneando carpetas...")

for categoria in categorias:
    ruta_categoria = os.path.join(carpeta_img, categoria)
    imagenes = []
    
    # Verificamos si la carpeta existe
    if os.path.exists(ruta_categoria):
        # Leemos los archivos
        for archivo in os.listdir(ruta_categoria):
            if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                # Guardamos la ruta relativa para la web
                # Ojo: Usamos '/' para web, no '\' de Windows
                ruta_web = f"img/{categoria}/{archivo}"
                imagenes.append(ruta_web)
        
        datos[categoria] = imagenes
        print(f"✅ {categoria}: {len(imagenes)} fotos encontradas.")
    else:
        print(f"⚠️ La carpeta {ruta_categoria} no existe.")

# Escribimos el archivo JS
contenido_js = f"const galeriaDatos = {json.dumps(datos, indent=4)};"

with open(archivo_salida, 'w', encoding='utf-8') as f:
    f.write(contenido_js)

print(f"\n✨ ¡Listo! Se ha creado el archivo '{archivo_salida}'.")