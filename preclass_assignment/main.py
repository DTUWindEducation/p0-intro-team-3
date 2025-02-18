import functions as fn

#es1
word= "world"
fn.greet(word)


#ese2    
l1=145
l2=155
l3=135
fn.goldilocks(l1)
fn.goldilocks(l2)
fn.goldilocks(l3)

#ese3
list1 = [1, 2, 3]  # Rimuovo le parentesi tonde extra
print(fn.square_list(list1))

#ese4
lim_up = 30
print(fn.fibonacci_stop(lim_up))

#ese5
x = [-1, 2, 8, 95]  # "raw" pitch angle at four time steps
status = [1, 0, 1, 0]  # status signal
print(fn.clean_pitch(x, status))
