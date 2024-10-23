# ejercicio

try:
    print(10/1)

    my_list = [1, 2, 3, 4]
    print(my_list[4])

except Exception as e:
    print(f"Error de syntaxis: {e}")

"""
Extra((
"""

def process_params(parameters: list):
    
    try:
        print(parameters[2])

    except Exception as e:
        print(f"Se ha producido un error: {e}")


process_params([1,2,3])