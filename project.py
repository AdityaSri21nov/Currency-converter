# Project to make a currency Generator
currency={"USD":81.77,
          "EUR":84.71,
          "INR":1,
          "POUND":98,
          "CAD":61.11,
          "CNY":11.41,
          "RUB":1.35,
          "AED":22.41} # Add more currency here


menu={"US Dollar":"USD",
      "EURO":"EUR",
      "Indian Rupee":"INR",
      "British":"POUND",
      "Canadian Dollar":"CAD",
      "Chinese yuan":"CNY",
      "Russian ruble":"RUB",
      "United Arab Emirates dirham":"AED"
      }
def convert(c1,a,c2):    
        if(c2=="INR"):
            print("The Currency After Converting %s into %s is"%(c1,c2),(amount*currency[c1]))
        elif(c1=="INR"):
            print("The Currency After Converting %s into %s is"%(c1,c2),(amount/currency[c2]))
        else:    
            print("The Currency After Converting %s into %s is"%(c1,c2),amount/currency[c2]*currency[c1])
            
print("------------------------")           
print("|  Currency Converter  |")
print("------------------------")


while (True):
        print("{:30} : {}".format("Currency","Country Code"))
        print()
        for i in menu:
                print("{:30} : {}".format(i,menu[i]))
        print()
        while True:
                c1=input("Enter The Currency: ") #The Currency given
                c2=input("Enter The Currency you want to convert to: ") # The currency you want to covert the amountUSD
                amount= eval(input("Enter The Amount: ")) # The amount in the given currency
                print()
                if (c1 in currency) and (c2 in currency):
                        break
                else:
                        print("Invalid Currency Code")
                        print()
        convert(c1,amount,c2)
        x=input("Is you want to convert more(Y/N): ")
        print()
        if x in "Nn":
                print("-------------------")
                print("| Have a nice day |")
                print("-------------------")
                break
        else:
                continue
