import matplotlib.pyplot as plt
import numpy as np

N_NUMBER = 256

def main(num):
    for i in reversed(range(num)):
        if i % 4 == 0:
            print(i)

def single_graph(num, option=None):
    plot_array = []
    c = 0; i = 0
    while (True):
        if c == 0:
            c = num
        if c % 2 == 0:
            c = c / 2
            plot_array.append([i, c])
        else:
            c = c * 3 + 1
            plot_array.append([i, c])
        if c == 1:
            break;
        i += 1
    a, b = zip(*plot_array)
    if (option != None):
        return a, b
    plt.plot(a, b, marker = "o", linestyle = "--")
    plt.show()

def multiple_graphs(nums):
    for num in nums:
        a, b = single_graph(num)
        plt.plot(a, b, marker = ".", linestyle = "--")
    
if __name__ == '__main__':
    option = input("Enter a option: ")
    if option == 1:
        a = input("Enter a Value: ")
        single_graph(input("Enter a Value: "))
  