#This This program is to find resistance, voltage and current using Ohm's law.
#The maximum number of errors are solved in this python source code. Code with No Error ;)
#For more codes visit https://thenextlevelcode.blogspot.com/

#function for addition

def addition(x,y):
    return (x+y)

#function for substraction

def substract(x,y):
    return(x-y)

# function for dividation

def divide(x,y):
    return(x/y)

#Function multiplication

def multiply(x,y):
    return(x*y)

print("Find Resistance,Current & Voltage using Ohm's Law\n")

while True:
    print('1. Calculate Voltage \n2. Calculate Resistance \n3. Calculate Current\n4. Exit Program')
    choose = input('Select The Number (1/2/3/4) : ')
    if choose in '1' '2' '3' '4':
        if choose == '1' :
            print("-- Calculating Voltage --")
            try :
                Resistance = float(input('Enter Resistance :'))
                Current = float(input('Enter Current :'))
                Resistance == Current == float()
                Voltage = float(multiply(Resistance, Current))
                print("Voltage =", Voltage)
            except ValueError:
                print("The input was not a valid number.")

        elif choose == '2' :
            print("-- Calculating Resistance --")
            try :
                Voltage2 = float(input('Enter Voltage :'))
                Current2 = float(input('Enter Current :'))
                Voltage2 == Current2 == float()
                Resistance2 = float(divide(Voltage2,Current2))
                print("Resistance =", Resistance2)
            except ValueError:
                print("The input was not a valid number.")

        elif choose == '3' :
            print("-- Calculating Current --")
            try:
                Voltage3 = float(input('Enter Voltage :'))
                Resistance3 = float(input('Enter Resistance :'))
                Voltage3 == Resistance3 == float()
                Current3 = float(divide(Voltage3,Resistance3))
                print("Current =", Current3)
            except ValueError:
                print("The input was not a valid number.")


        elif choose == '4':
            break
    else:
        print('**Invalid input**')

print("****Thanks For Using Calculator****")
print('Run Program again for using')
