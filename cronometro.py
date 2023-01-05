import time

def cronometro(tempo):
    while tempo:
        minutos, segundos = divmod(tempo, 60)
        timer = "{:02d}: {:02d}".format(minutos, segundos)
        print(timer, end="\r")
        time.sleep(1)
        tempo -= 1

    print("Contagem completa!")

try:
    tempo = input("Em segundos, digite segundos: ")
    cronometro(int(tempo))

except ValueError:
    print("Digite somente números")


