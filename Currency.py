while True:
    Pesos= (float)(input("How many pesos do you have left? "))
    Peru= (float)(input("How many soles do you have left? "))
    Brazil= (float)(input("How many Brazilian reais (BRL) do you have left? "))

    PesosUSD = (Pesos *.00024)

    PeruUSD = (Peru * .027)

    BrazilUSD = (Brazil * .17)

    TotalUSD = (PesosUSD + PeruUSD + BrazilUSD)

    Answer = input("Are these the right values?\n"
                    "Pesos {Pesos}\n"
                    "Peru {Peru}\n"
                    "Brazil {Brazil}\n"
                    "(Yes/No)")
    if Answer.lower() == "yes":
            print ("You have around:", TotalUSD, "USD")
            break
    else:
        print ("Try again, hoe")
   