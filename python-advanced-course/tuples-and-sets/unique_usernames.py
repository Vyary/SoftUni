number_of_usernames = int(input())
set_of_usernames = {input() for _ in range(number_of_usernames)}

print(*set_of_usernames, sep="\n")


"""                     Task:
Write a program that reads from the console a sequence of N usernames and keeps a
collection only of the unique ones. On the first line, you will receive an integer N.
On the next N lines, you will receive a username. Print the collection on the console
(the order does not matter):

Example:
Input:
6
George
George
George
Peter
George
NiceGuy1234
Output:
George
Peter
NiceGuy1234
"""
