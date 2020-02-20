def add(x,y):
    return x+ y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def check_if_user_has_to_finish():
    
    ok_to_finish = False
    user_input_accept = False
    
    while not user_input_accept:
        user_input = input("Do you want to finish?(y/n): ")
        if user_input == 'y':
            user_input_accept = True
            ok_to_finish = True
        elif user_input == 'n':
            ok_to_finish = False
            user_input_accept = True
        else:
            print("Respones must be (y/n), please try again")
    return ok_to_finish
    

        
        
def get_user_choice():
    input_ok = False
    while not input_ok:
        print("Menu Options are: ")
        print("\t1. Add")
        print("\t2. subtract: ")
        print("\t3. multiply: ")
        print("\t4. divide: ")
        print("---------------")
        user_selection = input("Please make a selection: ")
        if user_selection in ('1','2','3','4'):
            input_ok = True
        else:
            print("Invaild input, must be in (1-4)")
    print('------------------')
    return user_selection

def get_number_from_user():
    num1 = get_integer_input("Input the first number: ")
    num2 = get_integer_input("Input the second number: ")
    return num1,num2
    
def get_integer_input(message):
    value_as_string = message
    while not value_as_string.isnumeric():
        print("The input must be a integer")
        value_as_string = input(message)
    return int(value_as_string)
        
    
        
print("Simple Calculator App")
finished = False
while not finished:
    result = 0
    menu_choice = get_user_choice()
    n1,n2 = get_number_from_user()
    
    if menu_choice == '1':
        result = add(n1,n2)
    elif menu_choice == '2':
        result = subtract(n1,n2)
    elif menu_choice == '3':
        result = multiply(n1,n2)
    elif menu_choice == '4':
        result = divide(n1,n2)
    print("Result: ",result)
    print("---------------")
    finished = check_if_user_has_to_finish()
    
print("bye")
    
        
        
        
