serie = "N-03"

'''if serie == "N-01":
    print("samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")    
else:
    print("No se encontro") '''  

match serie:
    case "N-01":
        print("samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")    
    case _:
        print("No se encontro")  