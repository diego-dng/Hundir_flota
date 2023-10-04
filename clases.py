import funciones

class tablero:
    """
    Clase del tablero de juego.

    Atributos:
        
    """
    
    tipo = "tablero"
    tamaño_y = 10
    tamaño_x = 10 

    def __init__(self, id:int, dict_barcos:dict, ):

        """
        Atributos particulares a cada tienda

        Args:
            nombre (str): nombre de la tienda
            direccion (str): dirección de la tienda
            n_empleados (int): número de empleados de la tienda
            ventas_3m (list): lista de las ventas de los últimos 3 meses ordenado de más lejano a más cercano
        """

        self.id = id
        self.dict_barcos = dict_barcos
        funciones.crear_tablero()