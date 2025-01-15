def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    while True:
        print("\nConversor de Temperatura")
        print("1. Celsius para Fahrenheit")
        print("2. Celsius para Kelvin")
        print("3. Fahrenheit para Celsius")
        print("4. Fahrenheit para Kelvin")
        print("5. Kelvin para Celsius")
        print("6. Kelvin para Fahrenheit")
        print("0. Sair")

        try:

            opcao = input("\nEscolha uma opção (0-6): ")

            if opcao == "0":
                print("Obrigado por usar o conversor!")
                break
            temperatura = float(input("Digite a temperatura: "))

            if opcao == "1":
                resultado = celsius_para_fahrenheit(temperatura)
                print(f"{temperatura}ºC = {resultado:.2f}ºF")
            elif opcao == "2":
                resultado = celsius_para_kelvin(temperatura)
                print(f"{temperatura}ºC = {resultado:.2f}K")
            elif opcao == "3":
                resultado = fahrenheit_para_celsius(temperatura)
                print(f"{temperatura}ºF = {resultado:.2f}ºC")
            elif opcao == "4":
                resultado = fahrenheit_para_kelvin(temperatura)
                print(f"{temperatura}ºF = {resultado:.2f}K")
            elif opcao == "5":
                resultado = kelvin_para_celsius(temperatura)
                print(f"{temperatura}K = {resultado:.2f}ºC")
            elif opcao == "6":
                resultado = kelvin_para_fahrenheit(temperatura)
                print(f"{temperatura}K = {resultado:.2f}ºF")
            else:
                print("Opção inválida!")

        except ValueError:
            print("Erro. Digite apenas números!")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()