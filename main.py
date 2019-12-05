import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
print("Version: 0.2 (Alpha)")
print("Support Raspberry Pi: Zero")
pin = 0
stan = ""

WybranyJezyk = input("Select language (en/pl)\n")

while True:
    if(WybranyJezyk == "pl" or WybranyJezyk == "PL"):
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
        else:
            print("Błąd!")
            break




    elif (WybranyJezyk == "en" or WybranyJezyk == "EN"):
        WybranyPin = int(input("Select pin\n"))
        if(WybranyPin >= 1 and WybranyPin <= 27):
            pin = WybranyPin
            print("* Selected pin: "+str(pin)+" *")
        else:
            print("* Wrong pin *")
            break

        WybranyTryb = input("Please select mode (in/out)\n")
        if(WybranyTryb == "in"):
            print("<--- Pin "+str(pin)+" mode has been changed to input (in) --->")
            GPIO.setup(pin, GPIO.IN)
            stan = "in"
        elif(WybranyTryb == "out"):
            print("<--- Pin " + str(pin) + " mode has been changed to output (out) --->")
            GPIO.setup(pin, GPIO.OUT)
            stan = "out"
            WybranyStan = int(input("Select state (1/0)\n"))
            if(WybranyStan == 1):
                print("<--- Pin state " + str(pin) + " updated to 1 --->")
                GPIO.output(pin, GPIO.HIGH)
            elif(WybranyStan == 0):
                print("<--- Pin state " + str(pin) + " updated to 0 --->")
                GPIO.output(pin, GPIO.LOW)
        else:
            print("Wrong state!")
            break

        print("What now?")

        CoDalej = input("next / exit\n")

        if(CoDalej == "next"):
            continue
        elif(CoDalej == "exit"):
            break
        else:
            print("Error!")
            break
