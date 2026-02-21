#Tax Calculation
# salary=int(input("Enter your salary:"))
# if(salary < 30000):
#     print("Final tax applied to your salary is 5%")
# elif(salary >30000 and salary<=70000):
#     print("Final tax applied to your salary is 15%")
# elif(salary >70000):
#     print("Final tax applied to your salary is 25%")

#EVEN number between A and B:
# a=int(input("Enter 1st Number:"))
# b=int(input("Enter 2nd Number:"))
# def even(a,b):
#     for i in range(a,b):
#         if(i%2==0):
#             print(i)
    
# even(a,b)

#Number of Digits in a Number:
# num=int(input("Enter a number to print the didgits of it:"))
# count=0
# while num>0:
#     print(num%10)
#     num= num //10
#     count +=1
# print("Number of Digits in given numberis :",count)

#Count of Digits in a number:
# sum=0
# while num>0:
#     digit=num%10
#     sum=sum+digit
#     num=num //10

# print("Count of Digits in given number:",sum)

# Numbers from 1 - 100 Divisible from 3 and 5:
 print("Numbers between 1 - 100 divisible from 3 and 5 both:")
 for i in range(1,100):
     if(i%3==0 and i%5==0):
        print(i)

#positive and negative numbers until Quit
# while(True):
#     print("---------")
#     print("1.Enter number ")
#     print("2.Exit")
#     choice=int(input("Enter the choice as per given menu:"))
#     match choice:
#         case 1:
#             num=int(input("Enter a number to print the didgits of it:"))
#             if(num>0):
#                 print("Number is Positive--")
#             else:
#                 print("Number is Negative--")
#         case 2:
#             print("Exiting the loop...")
#             break
#         case _:
#             print("Enter valid input")

