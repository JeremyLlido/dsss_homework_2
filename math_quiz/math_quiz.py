import random

def generation_random_integer(min, max):
    """
    Generation of a random integer between a given min and a max value.
    
    Parameters:
    min (int): The minimum value of the range.
    max (int): The maximum value of the range.
    
    Returns:
    int: A random integer between min and max.
    """
    return random.randint(min, max)


def random_operator_selection():
    """
    Selection of a mathematical operator from '+', '-', and '*'.
    
    Returns:
    str: A randomly chosen mathematical operator.
    """
    return random.choice(['+', '-', '*'])


def elementary_operation_calculations(num1, num2, operator):
    """
    Generation of an elementary mathematical operation as a string and the correct answer.

    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.
    operator (str): The mathematical operator.

    Returns:
    tuple: A string representing the problem and the correct answer.
    """
    calculation = f"{num1} {operator} {num2}"
    # Calculate the result based on the operator
    
    if operator == '+': 
        result = num1 + num2   # bug fixed
    elif operator == '-': 
        result = num1 - num2   # bug fixed
    
    else: 
        result = num1 * num2
    return calculation, result

def math_quiz():
    """
    Creation of a mathematical Quiz.
    The score is displayed at the end of the game.
    """
    score = 0 #initialisation
    total_questions = 5 # number of questions

    # introduction message
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with basic math operations, and you need to provide the correct answers.")

    for question in range(total_questions):
        
        #Generation of two random numbers and a random operator
        num1 = generation_random_integer(1, 10);
        
        num2 = generation_random_integer(1, 10);
        
        operator = random_operator_selection()
        
        # Generation of a calculation and the associated result
        calculation, result = elementary_operation_calculations(num1, num2, operator)
        
        print(f"\nCalculation: {calculation}") # Display the calculation for the user
        
        # User input with error handling
        
  # Loop until the user provides a valid integer answer
        while True:
            try:
                user_answer = input("Your answer: ")
                # Attempt to convert user input to integer
                user_answer = int(user_answer)
                break  # Exit loop if input is a valid integer
            except ValueError:
                # Error message if input is not an integer
                print("Invalid input. Please enter an integer, not a floating-point number or text.")

        # Check if the user's answer is correct
        if user_answer == result:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {result}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
