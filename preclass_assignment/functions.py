# function es 1

def greet(name):
    return print("Hello, " + name + "!")


#function es 2
def goldilocks(l):
    if l>=140 and l<=150:
        return print("Just right. :)")
    elif l< 140:
        return print("Too small!")
    else:
        return print("Too large!")
    
#function es 3
def square_list(nums):
    return [num**2 for num in nums]  # List comprehension per semplificare

#function es 4
def fibonacci_stop(lim):
    fib = [1, 1]  # Lista iniziale con i primi due numeri di Fibonacci
    while fib[-1] + fib[-2] < lim:  # Controlla la somma prima di aggiungerla
        fib.append(fib[-1] + fib[-2])  # Aggiunge il nuovo numero

    return fib


#funcion es 5
def clean_pitch(x, status):
    clean_sig=[]
    for i in range(len(x)):
        if (x[i] <=0 or x[i]>= 90) and status[i]!=0:
           clean_sig.append(-999)
        else:
            clean_sig.append(x[i])
    return clean_sig