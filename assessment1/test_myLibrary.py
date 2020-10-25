"""
Crude tests for myLibrary. Should probably be proper unit tests.
"""
import myLibrary

myLibrary.inputInt("Input int: ")
myLibrary.inputInt("Input int greater or equal to 0: ", 0)
myLibrary.inputInt("Input int between 0-10 (inclusive): ", 0, 10)

myLibrary.inputFloat("Enter a float: ")
myLibrary.inputNonZeroFloat("Input a non-zero float: ")

l = [4,7,2,3,1,9,0,6,5,8]
myLibrary.bubble(l)
print(l)

myLibrary.testLab1()

myLibrary.chartList(l)

print(myLibrary.linear(2, 4))

print(myLibrary.quadSolver(1, 8, 12))

print(myLibrary.getUser(3))

print(myLibrary.getAv(myLibrary.getUser(3)))
print(myLibrary.getAv(myLibrary.getUser(4)))

print(myLibrary.slicer([1,2,3,4,5,6]))
print(myLibrary.slicer([1,1,1,1,6,6,6]))
