def get_inputs():                                 #users select inputs here
    input_number = int(input("Enter the number of inputs: "))
    inputs = []
    
    for i in range(input_number):
        inp = input("Enter the input (0 or 1): ") #McCulloch-Pitts Neural Model only accepts binary inputs.
        if inp in ("0", "1"):
            inputs.append(int(inp))
        else:
            print("McCulloch-Pitts Neural Model only accepts digit inputs.")
            exit()
    
    return inputs

def mcculloch_pitts_model(inputs, func_select):   #user select the function want to use here
    total_sum = sum(inputs)
    input_number = len(inputs)

    if func_select == 1:  #AND Function
        bias = input_number - 1
        return 1 if total_sum >= bias else 0
    elif func_select == 2:  #OR Function
        return 1 if total_sum > 0 else 0
    elif func_select == 3:  #NOR Function
        return 0 if total_sum > 0 else 1
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
