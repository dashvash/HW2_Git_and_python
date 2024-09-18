def fun_minus(a,c):
   return float(a) - float(c)

def main():
    line = str(input()).split()
    num_1 = line[0]
    num_2 = line[2]
    operator = line[1]
    if operator == "-": 
      return fun_minus(num_1,num_2)
