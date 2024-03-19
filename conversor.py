class Conversor:
    def __init__(self, numero):
        self.entero = numero
        self.romano = ""
    
    def convertirARomano(self) -> None:
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

        for valor, letra in lista.items():
            while self.entero >= valor:
                self.romano += letra
                self.entero -= valor
        print(f"El número romano es: {self.romano}")

    def convertirANumero(self) -> None:
        lista = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100, 
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        
        numero_entero = 0
        x = 0
        while x < len(self.romano):
            if x + 1 < len(self.romano) and self.romano[x:x+2] in lista:
                numero_entero += lista[self.romano[x:x+2]]
                x += 2
            else:
                numero_entero += lista[self.romano[x]]
                x += 1
        print(f"El número entero es: {numero_entero}")


        