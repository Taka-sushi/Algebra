from sympy import symbols, Eq
bt = ""
question = input("What is your level of Algebra? Please write a number between 1 - 12 :) ")
if question == "1":
  question1_1 = input("test")
if question == "2":
  question2_1 = input("test")
if question == "3":
  print("test")
if question == "4":
  print("test")
if question == "5":
  print("test")
if question == "6":
  print("test")
if question == "7":
  print("test")
if question == "8":
  print("test")
if question == "9":
  question9_1 = input("What are you learning right now? If it is expanding, type 1. If it is factorising, type 2 :) ")
  if question9_1 == "1":
    question9_2 = input("Are you familiar with expanding polynomial expressions? Type 1 for yes and 2 for no. ")
  if question9_1 == "2":
    question9_2 = input("Are you familiar with the difference of 2 squares? Type 1 for yes and 2 for no. ")
    if question9_2 == "1":
      question9_3 = input("Factorise x^2-9")
    elif question9_2 == "2":
      question9_4 = input("When an expression can be viewed as the difference of two perfect squares, i.e. a²-b², then we can factor it as (a+b)(a-b). For example, x²-25 can be factored as (x+5)(x-5). This method is based on the pattern (a+b)(a-b)=a²-b², which can be verified by expanding the parentheses in (a+b)(a-b). Do you understand? Type 1 for yes and 2 for more information. ")
      if question9_4 == "1":
        x = lines[36]
        print(x)
      if question9_4 == "2":
        print("Find more information here :) https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratics-multiplying-factoring/x2f8bb11595b61c86:factor-difference-squares/v/difference-of-squares-intro#:~:text=When%20an%20expression%20can%20be,a%2Bb)(a%2Db).")
    else:
      print("Print number 1 or 2 please :)")
      x = lines[38]
      print(x)
if question == "10":
  print("test")
if question == "11":
  print("test")
if question == "12":
  print("test")