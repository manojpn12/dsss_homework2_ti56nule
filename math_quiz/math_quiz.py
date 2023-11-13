import random


def number_range(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def math_operators():
    return random.choice(['+', '-', '*'])


def math_ques(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2 #addition of 2 numbers
    elif o == '-': a = n1 - n2 #subtraction of 2 numbers
    else: a = n1 * n2    #multiplication of 2 numbers
    return p, a

def math_quiz():
    point = 0
    tot_ques = 3   #total number of questions in the the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(tot_ques):
        n1=number_range(1, 10); n2 = number_range(1, 5); o = math_operators()

        PROBLEM, ANSWER = math_ques(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            point += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {point}/{tot_ques}")

if __name__ == "__main__":
    math_quiz()
