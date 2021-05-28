"""
Simulates a magic eight ball.
Prompts the user to type a yes or no question and gives
a random answer from a set of prefabricated responses.
"""
import random

def main():
    # Fill this function out!
    
    question = input("Ask your question: ")
    while question != "":
        response = get_response(random.randint(0,6))
        print(response)
        question = input("Ask your question: ")

def get_response(number):
    if number == 0:
        return "As I see it, yes."
    if number == 1:
        return "Ask again later."
    if number == 2:
        return "Better not to tell you now"
    if number == 3:
        return "Cannot predict now"
    if number == 4:
        return "Concentrate and ask again"
    if number == 5:
        return "Don't count on it"
    if number == 6:
        return "It is certain"

if __name__ == "__main__":
    main()
