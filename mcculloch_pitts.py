def get_inputs():                                 #users select inputs here
    input_number = int(input("Enter the number of inputs: "))
    inputs = []
    
    for i in range(input_number):
        inp = input("Enter the input (0 or 1): ") #McCulloch-Pitts Neural Model only accepts binary inputs.
        if inp in ("0", "1"):
            inputs.append(int(inp))
        else:
            print("McCulloch-Pitts Neural Model only accepts binary inputs.")
            exit()
    
    return inputs

def bias(inputs, fbias):     #func that sums inputs and subtracts the bias from them
    total_sum = sum(inputs)
    input_number = len(inputs)

    return total_sum-fbias

def mcculloch_pitts_model(inputs, func_select):   #user select the function want to use here
    input_number = len(inputs)
    
    if func_select == 1:  #AND Function
        fbias=input_number
        return 1 if bias(inputs, fbias)>=0 else 0 #AND Activation Function
    elif func_select == 2:  #OR Function
        fbias=1
        return 1 if bias(inputs, fbias)>=0 else 0 #OR Activation Function
    elif func_select == 3:  #NOR Function
        fbias=1
        return 0 if bias(inputs, fbias)>=0 else 1 #NOR Activation Function
    else:
        print("Invalid function selection.")
        exit()

def main():   #main 
    inputs = get_inputs()
    
    print("\nSelect the function to use:\n1. AND Function\n2. OR Function\n3. NOR Function")
    
    
    try:
        func_select = int(input("Enter function number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit()

    output = mcculloch_pitts_model(inputs, func_select)
    print(f"Output: {output}")

if __name__ == "__main__":
    main()
