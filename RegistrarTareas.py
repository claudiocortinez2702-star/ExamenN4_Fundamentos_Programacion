# Nombre: Claudio Cortinez
# Asignatura: Fundamentos de Programacion
# Examen: Numero 4 

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar tarea")
    print("2. Buscar tarea")
    print("3. Eliminar tarea")
    print("4. Actualizar estado")
    print("5. Mostrar tareas")
    print("6. Salir")
    print("=====================================")

def solicitar_opcion():
    try:
        opcion = int(input("Seleccione una opción: "))
        return opcion
    except ValueError:
        return -1

def validar_descripcion(descripcion):
    return len(descripcion.strip()) > 0

def validar_prioridad(prioridad_str):
    try:
        prioridad = int(prioridad_str)
        return 1 <= prioridad <= 10
    except ValueError:
        return False

def validar_tiempo(tiempo_str):
    try:
        tiempo = float(tiempo_str)
        return tiempo > 0
    except ValueError:
        return False

def agregar_tarea(lista_tareas):
    desc = input("Ingrese la descripción de la tarea: ")
    prio_str = input("Ingrese la prioridad (1 al 10): ")
    tiempo_str = input("Ingrese el tiempo estimado en horas: ")
    
    v_desc = validar_descripcion(desc)
    v_prio = validar_prioridad(prio_str)
    v_tiempo = validar_tiempo(tiempo_str)
    
    if not v_desc:
        print("Error: La descripción no puede estar vacía ni ser solo espacios en blanco.")
    if not v_prio:
        print("Error: La prioridad debe ser un número entero entre 1 y 10.")
    if not v_tiempo:
        print("Error: El tiempo estimado debe ser un número decimal mayor que cero.")
        
    if v_desc and v_prio and v_tiempo:
        nueva_tarea = {
            "descripcion": desc.strip(),
            "prioridad": int(prio_str),
            "tiempo_estimado": float(tiempo_str),
            "completada": False
        }
        lista_tareas.append(nueva_tarea)
        print("Tarea agregada exitosamente.")
    else:
        print("No se pudo realizar el registro debido a datos inválidos.")

def buscar_tarea(lista_tareas, descripcion_buscar):
    for i in range(len(lista_tareas)):
        if lista_tareas[i]["descripcion"].lower() == descripcion_buscar.strip().lower():
            return i
    return -1

def actualizar_estado(lista_tareas):
    for tarea in lista_tareas:
        if tarea["prioridad"] >= 5:
            tarea["completada"] = True
        else:
            tarea["completada"] = False

def mostrar_tareas(lista_tareas):
    actualizar_estado(lista_tareas)
    
    print("\n=== LISTA DE TAREAS ===")
    if len(lista_tareas) == 0:
        print("No hay tareas registradas en el sistema.")
        return
        
    for tarea in lista_tareas:
        estado_str = "COMPLETADA" if tarea["completada"] else "PENDIENTE"
        print(f"Descripción: {tarea['descripcion']}")
        print(f"Prioridad: {tarea['prioridad']}")
        print(f"Tiempo estimado: {tarea['tiempo_estimado']}")
        print(f"Estado: {estado_str}")
        print("********************************************")

def main():
    lista_general_tareas = []
    
    while True:
        mostrar_menu()
        opc = solicitar_opcion()
        
        if opc == 1:
            agregar_tarea(lista_general_tareas)
            
        elif opc == 2:
            buscar = input("Ingrese la descripción de la tarea a buscar: ")
            pos = buscar_tarea(lista_general_tareas, buscar)
            
            if pos != -1:
                tarea = lista_general_tareas[pos]
                estado_str = "COMPLETADA" if tarea["completada"] else "PENDIENTE"
                print(f"\n[Tarea encontrada en la posición {pos}]")
                print(f"Descripción: {tarea['descripcion']}")
                print(f"Prioridad: {tarea['prioridad']}")
                print(f"Tiempo estimado: {tarea['tiempo_estimado']}")
                print(f"Estado: {estado_str}")
            else:
                print("Tarea no encontrada.")
                
        elif opc == 3:
            eliminar = input("Ingrese la descripción de la tarea que desea eliminar: ")
            pos = buscar_tarea(lista_general_tareas, eliminar)
            
            if pos != -1:
                lista_general_tareas.pop(pos)
                print("Tarea eliminada exitosamente.")
            else:
                print(f"La tarea '{eliminar}' no se encuentra registrada.")
                
        elif opc == 4:
            actualizar_estado(lista_general_tareas)
            print("Estados actualizados para todas las tareas en base a su prioridad.")
            
        elif opc == 5:
            mostrar_tareas(lista_general_tareas)
            
        elif opc == 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break
            
        else:
            print("Opción inválida. Intente de nuevo con un número del 1 al 6.")

if __name__ == "__main__":
    main()