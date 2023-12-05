import random

# Lista de nodos
nodos = ['NODO_A', 'NODO_B', 'NODO_C', 'NODO_D', 'NODO_E']

# Listas de VNF principales y de respaldo
vnf_principales = ['VNF_1', 'VNF_2', 'VNF_3', 'VNF_4', 'VNF_5']
vnf_respaldo = ['VNF_R1', 'VNF_R2', 'VNF_R3', 'VNF_R4', 'VNF_R5']

total_asignaciones = 1000
contador_cumplen_restriccion = 0

for i in range(total_asignaciones):
    print(f"Iteracion: {i}")
    asignacion = {}
    vnf_utilizados = set()
    valido = False

    for j in range(len(nodos)):
        vnf_principales_disponibles = random.sample(vnf_principales, len(vnf_principales))
        vnf_respaldo_disponibles = random.sample(vnf_respaldo, len(vnf_respaldo))
        asignacion = {nodo: {'principal': vnf_p, 'respaldo': vnf_r} for nodo, vnf_p, vnf_r in zip(nodos, vnf_principales_disponibles, vnf_respaldo_disponibles)}
        
        # Verificar si los VNF cumplen con la restricción
        valido = all(vnf_p[-1] != vnf_r[-1] for vnf_p, vnf_r in zip(vnf_principales_disponibles, vnf_respaldo_disponibles))

    # Mostrar la asignación actual
    for nodo, vnf in asignacion.items():
        print(f"{nodo}: Principal={vnf['principal']}, Respaldo={vnf['respaldo']}")

    # Contar la cantidad de asignaciones que cumplen con la restricción
    if valido:
        contador_cumplen_restriccion += 1

print(f"Total de asignaciones que cumplen con la restriccion: {contador_cumplen_restriccion} de {total_asignaciones}")


