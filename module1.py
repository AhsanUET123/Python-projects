print("ASSALMALIKUM! Welcome to our Chai shop")
name =input("What's your name?\n")
if name=="Malang" or name=="Khan":
    evil_status=input("Are you Evil\n")
    if evil_status== "yes":
       print("You are not welcome here")
       exit()
    

menu="black Tea, Doodhpati,Green Tea,Pink Tea"
print("Welcome Mr:"+name+" What you want "+ menu)
order=input()
price=int()
if order=="black Tea":
    price= 30
elif order=="Doodhpati":
    price= 50
elif order=="Green Tea":
    price= 40
elif order=="Pink Tea":
    price= 70
else:
   print("We dont have it")
   exit()


    
print("Sounds good we would ready "+order+ " for you")
print("Your total would be Rs:"+ (str(price)))

