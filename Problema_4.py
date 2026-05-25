# ============================================================
# Nombre del estudiante: David Araque Gulloso
# Grupo: 213022_58
# Programa: Ingeniería de Sistemas
# Código Fuente: Autoría propia
# Problema 4: Videoteca Digital
# ============================================================


# ==================================================
# MATRIZ DE DATOS INICIAL: [Título, Año, Calificación, Género]
# ==================================================
videoteca = [
    ["Inception", 2010, 8.8, "Ciencia Ficción"],
    ["Oppenheimer", 2023, 8.5, "Drama"],
    ["The Matrix", 1999, 8.7, "Ciencia Ficción"],
    ["Spider-Man: Across the Spider-Verse", 2023, 8.9, "Animación"],
    ["El Padrino", 1972, 9.2, "Drama"],
    ["Dune: Parte Dos", 2024, 8.7, "Ciencia Ficción"],
    ["Pobres criaturas", 2023, 7.9, "Comedia"]
]

# ==================================================
# FUNCIÓN PARA VALIDAR AÑO
# ==================================================
def validar_año(mensaje):
    """
    ¿PARA QUÉ? Validar que el año sea un número entero mayor a 0.
    ¿POR QUÉ? No existen años negativos ni año cero en la realidad.
    """
    while True:
        try:
            año = int(input(mensaje))
            if año > 0:
                return año
            else:
                print(" Error: El año debe ser mayor a 0. No se aceptan años negativos ni cero.")
        except ValueError:
            print(" Error: Ingrese un número entero válido.")

# ==================================================
# FUNCIÓN PARA VALIDAR CALIFICACIÓN
# ==================================================
def validar_calificacion(mensaje):
    """
    ¿PARA QUÉ? Validar que la calificación esté entre 1 y 10.
    ¿POR QUÉ? No se aceptan negativos, cero ni mayores a 10.
    """
    while True:
        try:
            calif = float(input(mensaje))
            if 1 <= calif <= 10:
                return calif
            else:
                print(" Error: La calificación debe estar entre 1 y 10. No se aceptan negativos ni cero.")
        except ValueError:
            print(" Error: Ingrese un número válido (ej: 8.5).")

# ==================================================
# FUNCIÓN PARA MOSTRAR CATÁLOGO
# ==================================================
def mostrar_catalogo(matriz):
    """
    ¿PARA QUÉ? Mostrar todos los títulos con su información completa.
    ¿POR QUÉ? Para que el usuario sepa qué hay antes de agregar/quitar.
    """
    if len(matriz) == 0:
        print("\n El catálogo está vacío.")
        return
    
    print("\n" + "=" * 80)
    print("CATÁLOGO COMPLETO DE LA VIDEOTECA")
    print("=" * 80)
    print(f"{'N°':<3} {'TÍTULO':<35} {'AÑO':<6} {'CALIF.':<8} {'GÉNERO'}")
    print("-" * 80)
    
    for i, fila in enumerate(matriz):
        print(f"{i+1:<3} {fila[0]:<35} {fila[1]:<6} {fila[2]:<8} {fila[3]}")
    
    print("=" * 80)
    print(f"Total: {len(matriz)} títulos\n")

# ==================================================
# FUNCIÓN PARA AGREGAR TÍTULO
# ==================================================
def agregar_titulo(matriz):
    """
    ¿PARA QUÉ? Permitir al usuario añadir nuevos títulos al catálogo.
    ¿POR QUÉ? Para que la videoteca pueda crecer dinámicamente.
    """
    print("\n--- AGREGAR NUEVO TÍTULO ---")
    
    titulo = input("Título: ").strip()
    
    # Validar año usando la función específica
    año = validar_año("Año de lanzamiento: ")
    
    # Validar calificación usando la función específica
    calificacion = validar_calificacion("Calificación (1-10): ")
    
    genero = input("Género: ").strip()
    
    # Agregar a la matriz
    matriz.append([titulo, año, calificacion, genero])
    print(f"\n '{titulo}' agregado exitosamente.")
    
    return matriz

# ==================================================
# FUNCIÓN PARA ELIMINAR TÍTULO
# ==================================================
def eliminar_titulo(matriz):
    """
    ¿PARA QUÉ? Permitir al usuario quitar títulos existentes.
    ¿POR QUÉ? Para mantener el catálogo actualizado.
    """
    if len(matriz) == 0:
        print("\n No hay títulos para eliminar.")
        return matriz
    
    mostrar_catalogo(matriz)
    
    while True:
        try:
            indice = int(input("\nNúmero del título a eliminar: ")) - 1
            if 0 <= indice < len(matriz):
                eliminado = matriz.pop(indice)
                print(f"\n '{eliminado[0]}' eliminado exitosamente.")
                break
            else:
                print(f"\n Número inválido. Debe ser entre 1 y {len(matriz)}.")
        except ValueError:
            print("\n Error: Ingrese un número válido.")
    
    return matriz

# ==================================================
# FUNCIÓN PARA CONTAR TÍTULOS QUE CUMPLEN CRITERIOS
# ==================================================
def contar_titulos_populares_recientes(matriz, umbral_calificacion, ano_limite):
    """
    ¿PARA QUÉ? Contar títulos que cumplen ambas condiciones.
    ¿POR QUÉ PARÁMETROS? Para que la función sea reutilizable con diferentes umbrales.
    
    Parámetros:
    - matriz: lista de listas con [título, año, calificación, género]
    - umbral_calificacion: valor mínimo de calificación (entre 1 y 10)
    - ano_limite: año mínimo de lanzamiento (mayor a 0)
    
    Retorna: número entero de títulos que cumplen
    """
    contador = 0
    titulos_cumplen = []  # ¿PARA QUÉ? Mostrar cuáles cumplen al final
    
    for fila in matriz:
        año = fila[1]
        calificacion = fila[2]
        
        if calificacion >= umbral_calificacion and año >= ano_limite:
            contador += 1
            titulos_cumplen.append(fila[0])
    
    return contador, titulos_cumplen

# ==================================================
# FUNCIÓN PARA EJECUTAR EL PROCESO DE CONTEO
# ==================================================
def ejecutar_conteo(matriz):
    """
    ¿PARA QUÉ? Ejecutar el proceso principal de conteo con criterios definidos por usuario.
    ¿POR QUÉ? Para permitir repetir el proceso con diferentes parámetros.
    """
    if len(matriz) == 0:
        print("\n No hay títulos en el catálogo. Agregue algunos primero.")
        return matriz
    
    print("\n" + "=" * 60)
    print("PROCESO DE CONTEO - MATERIAL POPULAR Y RECIENTE")
    print("=" * 60)
    
    # Solicitar criterios al usuario CON VALIDACIONES
    print("\n La calificación debe estar entre 1 y 10")
    umbral = validar_calificacion("Ingrese calificación mínima: ")
    
    print("\n El año debe ser mayor a 0 (no se aceptan negativos ni cero)")
    año_limite = validar_año("Ingrese año mínimo: ")
    
    # Ejecutar conteo
    total, titulos = contar_titulos_populares_recientes(matriz, umbral, año_limite)
    
    # Mostrar resultados
    print("\n" + "-" * 60)
    print(f"RESULTADO: {total} título(s) cumplen ambos criterios.")
    print(f"  • Calificación ≥ {umbral}")
    print(f"  • Año ≥ {año_limite}")
    
    if total > 0:
        print("\n Títulos que cumplen:")
        for titulo in titulos:
            print(f"  • {titulo}")
    else:
        print("\n No hay títulos que cumplan con los criterios.")
    
    print("-" * 60)
    return matriz

# ==================================================
# MENÚ PRINCIPAL
# ==================================================
def menu_principal():
    """
    ¿PARA QUÉ? Controlar el flujo del programa con opciones repetitivas.
    ¿POR QUÉ? Para que el usuario decida qué hacer sin reiniciar el programa.
    """
    matriz = [fila[:] for fila in videoteca]  # Copia profunda para no modificar la original
    
    while True:
        print("\n" + "=" * 50)
        print("VIDEOTECA DIGITAL - MENÚ PRINCIPAL")
        print("=" * 50)
        print("1. Ver catálogo completo")
        print("2. Agregar nuevo título")
        print("3. Eliminar título")
        print("4. Realizar proceso de conteo (popular + reciente)")
        print("5. Salir")
        print("=" * 50)
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        # ¿POR QUÉ USAR if-elif? Para ejecutar acción según lo que elija el usuario.
        if opcion == "1":
            mostrar_catalogo(matriz)
        
        elif opcion == "2":
            matriz = agregar_titulo(matriz)
        
        elif opcion == "3":
            matriz = eliminar_titulo(matriz)
        
        elif opcion == "4":
            matriz = ejecutar_conteo(matriz)
        
        elif opcion == "5":
            print("\n Gracias por usar la Videoteca Digital. ¡Hasta luego!")
            break
        
        else:
            print("\n Opción inválida. Seleccione 1, 2, 3, 4 o 5.")

# ==================================================
# EJECUCIÓN PRINCIPAL
# ==================================================
if __name__ == "__main__":
    print("=" * 50)
    print("BIENVENIDO A VIDEOTECA DIGITAL")
    print("=" * 50)
    print("\n NOTA: No se aceptan años negativos, años cero ni calificaciones negativas.")
    menu_principal()