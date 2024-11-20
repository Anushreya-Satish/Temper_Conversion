print ("Temperature Conversion ")
input1 = int ( input ( "If you want to convert temperature from Celsius to Fahrenheit type 1 / If you want to convert temperature from Fahrenheit to Celsius type 2 : "))
temp = int( input ("What is the temperature ? : "))
new = 0

if input1 == 1 :
    print ("Conversion from Celsius to Fahrenheit")
    new = (9*temp)/5 + 32
    print (new, " °Fahrenheit")
elif input1 == 2 :
    print ("Conversion from Fahrenheit to Celsius")
    new = (5*(temp-32))/9
    print (new, " °Celsius")
else :
    print ("The user prompt is not defined. Please, choose as per the menu (1/2)")
