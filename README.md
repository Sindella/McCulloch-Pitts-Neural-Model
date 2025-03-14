# McCulloch-Pitts Neural Model

## Introduction
The **McCulloch-Pitts Neural Model** is one of the earliest mathematical models of a neural network. It is a simple binary threshold neuron model that mimics the basic functioning of biological neurons. This model is primarily used to implement basic logic functions such as AND, OR, and NOR.

This repository contains a Python implementation of the McCulloch-Pitts model, allowing users to input binary values and choose a logical function to process the inputs.

## How It Works
The McCulloch-Pitts neuron processes inputs using a weighted sum and a threshold (bias) to determine the output:

![image](https://github.com/user-attachments/assets/ab6c851d-4e7e-44eb-b2ae-00dee24005c7)

### Supported Logic Functions
- **AND Function:** Outputs 1 only if all inputs are 1.
- **OR Function:** Outputs 1 if at least one input is 1.
- **NOR Function:** Outputs 1 only if all inputs are 0.

## Code Explanation
The script takes the following steps:
1. **User Input:** The program asks the user for the number of binary inputs.
2. **Validation:** Ensures that only 0 and 1 are accepted as inputs.
3. **Function Selection:** The user selects one of the three logic functions (AND, OR, NOR).
4. **Computation:** The model computes the sum of inputs and applies the threshold condition for the selected function.
5. **Output:** Displays the result based on the logic function chosen.

### Example Usage
```shell
Enter the number of inputs: 3
Enter the input (0 or 1): 1
Enter the input (0 or 1): 0
Enter the input (0 or 1): 1

Select the function to use:
1. AND Function
2. OR Function
3. NOR Function
Enter function number: 1
Output: 0
```

## Installation & Execution
### Prerequisites
Ensure you have **Python 3.x** installed on your system.

### Running the Script
1. Clone the repository:
   ```bash
   git clone https://github.com/Sindella/McCulloch-Pitts-Neural-Model.git
   ```
2. Navigate to the project directory:
   ```bash
   cd McCulloch-Pitts-Neural-Model
   ```
3. Run the script:
   ```bash
   python mcculloch_pitts.py
   ```


