initalDisplay='''
            Sunway international Business School
            Maitedevi, Kathmandu'''
print(initalDisplay)

std_Name=input("\nEnter student name: ")
std_Address=input("Enter student Address: ")
std_faculty=input("Enter student Faculty: ")
std_Program=input("Enter student program: ")
std_intake=input("Enter student intake Year: ")
AppliedProgrammning, Communication, BasicEnterprenure, MobileProgramming, DataStructure = input("Enter marks of AppiedProgramming, Enter marks of Communication, Enter marks of BasicEnterprenure, Enter marks of MobileProgramming, Enter marks of DataStructure ").split(",")
totalMarks=int(AppliedProgrammning)+int(Communication)+int(BasicEnterprenure)+int(BasicEnterprenure)+int(DataStructure)
Percentage=int(totalMarks/5)
if Percentage>90:
    grade="A+"
elif  Percentage<90 and  Percentage>80:
    grade="A"
elif  Percentage<80 and  Percentage>70:
    grade="B+"
elif  Percentage<70 and  Percentage>60:
    grade="B"
elif  Percentage<60 and  Percentage>50:
    grade="C+"
elif  Percentage<50 and  Percentage>40:
    grade="D"
elif  Percentage<30:
    grade="E"
else:
        Print("ThankYou")
print(initalDisplay)
print(f"Student Name:{std_Name} \t Student Address:{std_Address}") 
print(f"Student Facutly:{std_faculty} \t Student Program:{std_Program}")
print(f"Intake:{std_intake}")
print(f"-------------------------------")
print(f"Student {std_Name} award as Grade {grade} ")
    
