"""
File I/O Lab
By: Jesse DeMarco

CSCI 110
Date: 04/21/2026

Program prompts user to enter name of the file that contains 10 integers.
It opens, reads and stores the numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
Program will then print the sorted lists to an output file along with the 
largest and smallest values in the list.

NOTE: All fixme's are each worth 10 points except for the FIXME1 which is worth 20 points
"""

from typing import List

totalInts = 10


def readData() -> List[int]:
    """Read data from a file.

    Returns:
        List[int]: List of integers
    """
    intList = []
    # FIXME1 (20 points):
    # Prompt user to input file name
    # open the file; read each number one line at a time;
    # and store it into intList list
    # close the file
    # return the intList
    inputFileName = input('Enter the input file name:')
    inputFile = open(inputFileName, 'r')

    for _ in range(totalInts):
        number = int(inputFile.readline().strip())
        intList.append(number)

    inputFile.close()
    return intList


def sortListInAscendingOrder(lstInts: List[int]):
    """Sort the provided list in ascending order.

    Args:
        lstInts (List[int]): the list to be sorted.
    """
    # FIXME2
    # sort lstInts list in ascending order
    lstInts.sort()


def sortListInDescendingOrder(lstInts: List[int]):
    """Sort the provided list in descending order.

    Args:
        lstInts (List[int]): the list to be sorted.
    """
    # FIXME3
    # sort lstInts in descending order
    lstInts.sort(reverse=True)


def printList(printFile, lstInts: List[int]):
    for n in lstInts:
        # FIXME4
        # write each value one line at a time to file
        # handled by printFile object.
        printFile.write(str(n) + '\n')
    printFile.write('\n')


def main():
    integers = []  # list to store integers
    integers = readData()
    outputFileName = input('Enter a file to write output to: ')
    printFile = open(outputFileName, 'w')
    printFile.write("Numbers entered:\n")
    printList(printFile, integers)
    # sort numbers
    sortListInAscendingOrder(integers)
    printFile.write("Numbers sorted in ascending order:\n")
    printList(printFile, integers)

    # FIXME5
    # Call sortListInDescendingOrder function
    sortListInDescendingOrder(integers)

    # FIXME6
    # Write the sorted list in descending order to the output file
    printFile.write("Numbers sorted in descending order:\n")
    printList(printFile, integers)
    # FIXME7
    # Print the largest number to the output file
    printFile.write("Largest number: " + str(integers[0]) + '\n')
    # FIXME8
    # Print the smallest number to the output file
    printFile.write("Smallest number: " + str(integers[-1]) + '\n')

    printFile.close()
    print('Done executing the program! Check the output file for results.')


# FIXME9
# Call main function if this module is run as the main module
if __name__ == "__main__":
    main()
