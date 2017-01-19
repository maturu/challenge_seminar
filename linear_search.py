#coding: utf-8
import sys
import numpy as np
from generate_algorithm import Generate
import sl2z

def main():
    # Constract 2 x 2 Identity Matrix
    target = np.eye(2)
    # List Initialization and (Min ~ Max) of Linear Search 
    list_size = 0
    max_matrix = np.eye(2)
    add_matrix = np.eye(2)
    # Result List value
    list_matrix = []
    list_data = []
    # loop value
    SEARCH_MAX = 10
    SEARCH_MIN = -10
    # Linear Search for 1 ~ 10
    for i in range(SEARCH_MIN, SEARCH_MAX + 1):
        for j in range(SEARCH_MIN, SEARCH_MAX + 1):
            for k in range(SEARCH_MIN, SEARCH_MAX + 1):
                for l in range(SEARCH_MIN, SEARCH_MAX + 1):
                   # Create Instance
                    gen = Generate()
                    target[(0, 0)] = i
                    target[(0, 1)] = j
                    target[(1, 0)] = k
                    target[(1, 1)] = l
                    # Judge element of SL(2, Z)
                    if sl2z.judge_sl2Z(target) == False:
                        continue
                    if sl2z.judge_sl2Z(target) == True :
                        print("")
                        print("----------------------")
                        print("Input :")
                        print(target)
                        print("----------------------")
                        # Set and Judge element of SL(2, Z)
                        gen.set_target(target)
                        gen.set_isShowProcess(True)
                        # Run Search
                        gen.proof()
                        # Judge loop final
                        for matrix in gen.get_exp_i_seed_matrix():
                            if matrix['type'] == 'omega':
                                sys.stdout.write('ω ^ ' + str(matrix['exp']))
                            elif matrix['type'] == 'sigma':
                                sys.stdout.write('σ ^ ' + str(matrix['exp']))
                            sys.stdout.write(' ')
                        print("")
                        #  Print Result
                        print("result :")
                        print(gen. get_result())
                        # Judge List largest
                        if len(gen.get_exp_i_seed_matrix()) > list_size:
                            list_matrix = []
                            list_data = []
                            list_size = len(gen.get_exp_i_seed_matrix())
                            data = gen.get_exp_i_seed_matrix()[:]
                            list_data.append(data)
                            max_matrix[0,0] = target[0,0]
                            max_matrix[0,1] = target[0,1]
                            max_matrix[1,0] = target[1,0]
                            max_matrix[1,1] = target[1,1]
                            list_matrix.append(max_matrix)
                        elif len(gen.get_exp_i_seed_matrix()) == list_size:
                            list_size = len(gen.get_exp_i_seed_matrix())
                            data = gen.get_exp_i_seed_matrix()[:]
                            list_data.append(data)
                            add_matrix[0,0] = target[0,0]
                            add_matrix[0,1] = target[0,1]
                            add_matrix[1,0] = target[1,0]
                            add_matrix[1,1] = target[1,1]
                            list_matrix.append(add_matrix)
                    #Garbage Collection
                    gen = None
        # Judge loop final
        if i == SEARCH_MAX and j == SEARCH_MAX and k == SEARCH_MAX and l == SEARCH_MAX:
            print("----------------------")
            print("")
            print("Max Result :")
            # Result print loop
            for i in range(0, len(list_matrix)):
                print(list_matrix[i])
                sys.stdout.write("=")
                for matrix in list_data[i]:
                    if matrix['type'] == 'omega':
                        sys.stdout.write('ω ^ ' + str(matrix['exp']))
                    elif matrix['type'] == 'sigma':
                        sys.stdout.write('σ ^ ' + str(matrix['exp']))
                    sys.stdout.write(' ')
                print("")
                print("----------------------")

if __name__ == '__main__':
    main()
