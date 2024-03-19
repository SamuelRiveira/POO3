from contactos import Filewriter

if __name__ == "__main__":
    def main():
        pruebaw = Filewriter("fileWriter.txt")
        pruebaw.write("Hola")
        pruebaw.close()

        pruebar = Filewriter("fileWriter.txt")
        print(pruebar.read())
        pruebar.close()

main()