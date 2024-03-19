from conversor import Conversor

def main()-> None:
    numero = Conversor(944)
    numero.convertirARomano()
    numero.convertirANumero()

if __name__ == "__main__":
    main()