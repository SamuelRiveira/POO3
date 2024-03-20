from contactos import Filewriter

if __name__ == "__main__":
    def main():
        pruebaw = Filewriter("fileWriter.csv")
        pruebaw.write("Hola")
        pruebaw.close()

        pruebar = Filewriter("fileWriter.csv")
        print(pruebar.read())
        pruebar.close()

main()