class Conversor:
    def __init__(self, entero:int = 0, romano:str = "") -> None:
        self.entero = entero
        self.romano = romano
    
    def convertir(self)-> None:
        lista = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

        result = ""
        for valor in lista.keys():
            while self.entero >= valor:
                self.romano += lista[valor]
                self.entero -= valor
        print(f"El número romano es: {self.romano}")