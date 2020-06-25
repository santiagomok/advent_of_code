
def compute_fuel(val):
    return (int(val / 3)) - 2

def compute_fuel_ext(val):
    #  print("val: {}".format(val))
    fuel = compute_fuel(val)
    if(fuel < 0): 
        # if negative fuel return 
        return 0
    else:
        # otherwise keep summing fuel requirement
        fuel += compute_fuel_ext(fuel)
    return fuel

     
count = 0
sum = 0
fuel_sum = 0 
fuel_sum_ext = 0 

f = open('day1_input.txt', 'r')
for line in f:
    sum += int(line)
    count += 1
    fuel_sum += compute_fuel(int(line))
    fuel_sum_ext += compute_fuel_ext(int(line))

print("count: {}".format(count))
print("sum: {}".format(sum))
print("fuel_sum: {}".format(fuel_sum))
print("fuel_sum_ext: {}".format(fuel_sum_ext))
#  print("fuel_sum_ext: {}".format(compute_fuel_ext(14)))
#  print("fuel_sum_ext: {}".format(compute_fuel_ext(1969)))

