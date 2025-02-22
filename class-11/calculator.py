q_num_1 = str(input("Enter First Number: "))
q_num_2 = str(input("Enter Second Number: "))
operator = str(input("Enter any operator: "))

class House:
    def num(self, num_1:str, num_2:str, operator: str):
        self.num1 = num_1 
        self.num2 = num_2
        if(operator == "+"):
            cal = eval(f"{q_num_1} {operator} {q_num_2}")

        elif(operator == "-"):
            cal = eval(f"{q_num_1} {operator} {q_num_2}")
        elif(operator == "/"):
            if(num_2 == 0):
                print("Math error")
            else:
                cal = eval(f"{q_num_1} {operator} {q_num_2}") 
        elif(operator == "*"):
            cal = eval(f"{q_num_1} {operator} {q_num_2}")
        else:
            print("Invalid operator")  
        
        result = cal     
        return result


myHouse = House()
print(myHouse.num(q_num_1, q_num_2, operator))