import random

def generate_random_integer(min_value, max_value):
    """
    Generates a random integer between min_value and max_value.
    
    Parameters:
    min_value (int): The minimum value of the range.
    max_value (int): The maximum value of the range.
    
    Returns:
    int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Randomly selects a mathematical operator from '+', '-', and '*'.
    
    Returns:
    str: A randomly chosen mathematical operator.
    """
    return random.choice(['+', '-', '*'])


def generate_problem_and_answer(n1, n2, operator):
    """
    Generates a math problem as a string and the correct answer.

    Parameters:
    n1 (int): The first number.
    n2 (int): The second number.
    operator (str): The mathematical operator.

    Returns:
    tuple: A string representing the problem and the correct answer.
    """
    problem = f"{n1} {operator} {n2}"
    # Calculate the correct answer based on the operator
    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    else:
        answer = n1 * n2
    return problem, answer


def math_quiz():
    """
    Main function of the math quiz game.
    The player will be presented with math problems and needs to provide correct answers.
    
    The score is displayed at the end of the game.
    """
    score = 0
    total_questions = 5  # Total number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate two random numbers and a random operator
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, correct_answer = generate_problem_and_answer(num1, num2, operator)
        print(f"\nProblem: {problem}")

        # User input with error handling
        while True:
            try:
                user_answer = int(input("Your answer: "))
                break  # Exit loop if input is valid
            except ValueError:
                print("That's not a valid number. Please enter a valid integer.")

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
