import matplotlib.pyplot as plt
# from sympy.ntheory.primetest import is_square 
import array as arr

N_NUMBER = 256

def main(num):
    for i in reversed(range(num)):
        if i % 4 == 0:
            print(i)

def single_graph(num, option=None):
    plot_array = []
    c = 0; i = 0; max_c = [0, 0]
    while (True):
        if c == 0:
            c = num
            plot_array.append([i-1, c])
            plt.text(i-1, c, c)
        if c % 2 == 0:
            c = c / 2
            plot_array.append([i, c])
            if c % 4 == 0 and c > max_c[0]:
                max_c = [c, i, num]
                plt.text(i, c, c)
            else:
                plt.text(i, c, c)
        else:
            c = c * 3 + 1
            plot_array.append([i, c])
            if c % 4 == 0 and c > max_c[0]:
                max_c = [c, i, num]
                plt.text(i, c, c)
            else:
                plt.text(i, c, c)
        if c == 1:
            plt.text(max_c[1], max_c[0], max_c[0], color="red")
            break;
        i += 1
    a, b = zip(*plot_array)
    if (option == 1):
        return a, b, max_c
    plt.plot(a, b, marker = "o", linestyle = "--")
    plt.show()
    
def multiple_graphs(nums):
    final_array = []; max_c = []
    for num in nums:
        a, b, max = single_graph(num, 1)
        max_c.append(max)
        plt.plot(a, b, marker = ".", markersize = 8, label=str(num))
    print(str(max_c))
    plt.legend()
    plt.show()

# def sort_by_num_max_value(max_c):
#     a, b, c = zip(*max_c)
#     unique_max = [set(a)]
#     sort_list = list()
#     for i in max_c:
#         if i[1] in unique_max:
            
def sum_of_break_points():
    pass
        
if __name__ == '__main__':
    while(True):
        option = raw_input("Enter a option: ")
        if option == "done":
            break;
        elif option == '1':
            single_graph(input("Enter a Value: "))
        elif option == '2':
            str_arr = raw_input('Enter values: ').split(' ')
            arr = [int(num) for num in str_arr]
            multiple_graphs(arr)
        else:
            print('Invalid Option, try again!')