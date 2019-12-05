import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
print("Version: 0.1 (Alpha)")
print("Support Raspberry Pi: Zero")
pin = 0
stan = ""

while True:
    WybranyPin = int(input("Wybierz pin\n"))
    if(WybranyPin >= 1 and WybranyPin <= 27):
        pin = WybranyPin
        print("* Zaznaczony został pin: "+str(pin)+" *")
    else:
        print("* Błędny pin *")
        break

    WybranyTryb = input("Wybierz tryb (in/out)\n")
    if(WybranyTryb == "in"):
        print("<--- Tryb pinu "+str(pin)+" został zmieniony na wejście (in) --->")
        GPIO.setup(pin, GPIO.IN)
        stan = "in"
    elif(WybranyTryb == "out"):
        print("<--- Tryb pinu " + str(pin) + " został zmieniony na wyjście (out) --->")
        GPIO.setup(pin, GPIO.OUT)
        stan = "out"
        WybranyStan = int(input("Wybierz stan (1/0)\n"))
        if(WybranyStan == 1):
            print("<--- Stan pinu " + str(pin) + " został zmieniony na 1 --->")
            GPIO.output(pin, GPIO.HIGH)
        elif(WybranyStan == 0):
            print("<--- Stan pinu " + str(pin) + " został zmieniony na 0 --->")
            GPIO.output(pin, GPIO.LOW)
    else:
        print("Błędny stan!")
        break

    print("Co chcesz zrobić dalej?")

    CoDalej = input("nastepny / zakoncz\n")

    if(CoDalej == "nastepny"):
        continue
    elif(CoDalej == "zakoncz"):
        break
