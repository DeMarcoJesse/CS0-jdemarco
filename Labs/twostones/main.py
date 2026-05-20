"""
Conditional Logic Lab
Updated By: Jesse DeMarco
CSCI 110 Lab
Date: 03/05/2026

Read and solve the Kattis problem: https://open.kattis.com/problems/twostones 

Algorithm Steps:
  1. Read the number of stones
  2. Check if the number of stones is odd or even
  3. Print the winner
    3.a. If the number is odd, Alice wins.
    3.b. Otherwise, Bob wins.
"""


def main():
    """Main function that solves the problem
    """
    # FIXME 1: read the number of stones #fixed#
    stones = int(input())
    # FIXME 2: call answer function passing the number of stones as an argument #fixed#
    result = answer(stones)
    # FIXME 3: print the answer as shown in the sample output #fixed#
    print(result)


def odd_even(number: int):
    """Checks if the number is odd or even

    Args:
        number (int): number to check odd or even

    Returns:
        str: 'odd' if the number is odd, 'even' otherwise
    """
    # FIXME 4: if the number divided by 2 has 0 remainder, return 'even'
    # otherwise, return 'odd' #fixed#
    if number % 2 == 0:
        ans = "even"
    else:
        ans = "odd"
    return ans


def answer(stone: int):
    """Creates the final answer and returns it given the number of stones

    Args:
        stone (int): number of stones

    Returns:
        str: 'Alice' if the number of stones is odd, 'Bob' otherwise
    """
    evenorodd = odd_even(stone)
    if evenorodd == "odd":
        return "Alice"
    else:
        return "Bob"


if __name__ == "__main__":
    main()
