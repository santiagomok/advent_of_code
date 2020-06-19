#!/usr/bin/env python3

with open('day2_input.txt') as f:
    for line in f.readlines():
        data_src = [int(x) for x in line.strip().split(',')]

#  data[1] = 12
#  data[2] = 2
#  print(len(data))
#  print("Before")
#  print(data)


def Intcode(data_arg, noun, verb):
    data = data_arg.copy()
    #  print(data)
    l_index = 0
    u_index = 3

    data[1] = noun
    data[2] = verb

    while(data[l_index] != 99):
        op_code = data[l_index]
        in_1 = data[data[l_index+1]]
        in_2 = data[data[l_index+2]]
        out_index = data[u_index]
        #  print("out_index: " + str(out_index))

        if(op_code == 1):
            data[out_index] = in_1 + in_2
        elif(op_code == 2):
            data[out_index] = in_1 * in_2

        # advance to next set
        l_index += 4
        u_index += 4
    return data[0]

print(Intcode(data_src,12,2))

for i in range(100):
    for j in range(100):
        if(Intcode(data_src, i,j) == 19690720):
            print("({},{}: {})".format(i,j,100*i+j))
