def initialDisplay():
    Display='''
            Sunway international Business School
        Maitedevi, Kathmandu'''
    print(Display)
    
def initialInput():
     c_name=input("\nEnter a Customer Name: ")
     c_Address=input("Enter a Customer Address: ")
     ConsumedUnit=int(input("Enter a total consumed unit: "))
     return c_name,  c_Address, ConsumedUnit
     
def Calculation(ConsumedUnit): 
    if  ConsumedUnit<=20:
        netcost=ConsumedUnit*4
    elif ConsumedUnit>20 and ConsumedUnit<=50:
        netcost=(20*4)+((ConsumedUnit-20)*7.5)
    elif ConsumedUnit>50 and ConsumedUnit<=150:
        totalcost=(20*4)+(30*7.5) + ((ConsumedUnit-50)*9.5)
        totaldiscount=5/100*((ConsumedUnit-50)*9.5)
        netcost=totalcost- totaldiscount
    elif ConsumedUnit>150 and ConsumedUnit<=250:
            totalcost=(20*4)+(30*7.5) + (100*9.5)+((ConsumedUnit-100)*11.5)
            discount=10/100*((ConsumedUnit-100)*11.5)
            totaldiscount= discount-5/100*(100*9.5)
            netcost=totalcost- totaldiscount
    elif ConsumedUnit>250:
            totalcost=(20*4)+(30*7.5) + (100*9.5)+(100*11.5)+((ConsumedUnit-250)*13.5)
            discount=10/100*((ConsumedUnit-250)*15)
            totaldiscount= discount-(5/100*(100*9.5)+10/100*(100*11.5))
            netcost=totalcost- totaldiscount
    else:
          print("ThankYou")
    return netcost, totalcost, totaldiscount
  
    
def informationDisplay(c_name,  c_Address, ConsumedUnit, netcost, totalcost, totaldiscount):
    print(f"Customer Name: {c_name} \t customer Address:{c_Address}") 
    print(f"Customer Consumed Unit:{ConsumedUnit} \t Total Amount to pay:{totalcost}") 
    print(f"Total Discount:{totaldiscount}  \t After Discount:{netcost}") 
    
 
initialDisplay()
c_name,  c_Address, ConsumedUnit = initialInput()
netcost, totalcost, totaldiscount = Calculation(ConsumedUnit)
initialDisplay()
informationDisplay(c_name,  c_Address, ConsumedUnit, netcost, totalcost, totaldiscount)