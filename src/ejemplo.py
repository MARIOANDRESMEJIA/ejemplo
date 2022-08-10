## codigo de ejemplo
import sys
from termios import VINTR
print("UNIVERSIDAD DE IBAGUE")
print("\t PROGRAMA DE ING.ELECTRONICA")

if __name__ == "__main__":
    Vin = float(sys.argv[1])
    R1 = float(sys.argv[2])
    R2 = float(sys.argv[3])

##    print("esto es aux:", aux)
    V0 = R1/(R1+R2)*Vin 
    print("V0 es igual a :", round(V0,4))