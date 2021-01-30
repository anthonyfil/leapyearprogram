print("This is a Leap Year Calculator")
inp = "y"
while(not inp.isdigit()):
    print("Enter a Year")
    inp = input()
year = int(inp)
if(year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            print(inp + " Is A Leap Year")  
        else:
            print(inp + " Is Not A Leap Year")

    else:
          print(inp + " Is A Leap Year")
else:
    print(inp + " Is Not A Leap Year")
