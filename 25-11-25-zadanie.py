
def sum(nums): #minavam prez chislata i gi subiram v sum
    sum = 0
    for i in nums:
        sum += i
    return sum

def sumrec(nums): #vzimam nai prednoto chislo na masiva i go maham ot masiva, dokato ne ostane samo poslednoto
                  #i ne oburnem v rekursiqta subiraiki vsichki poredni
    num = nums[0]
    if len(nums) == 1:
        return num
    nums.pop(0)
    return sumrec(nums) + num

def flipstring(input : str):
    len(input) - 1 
    newstr = ""
    for i in range(len(input) - 1, -1, -1): # tozi golqm range zima posledniq index, kazva range ot posled do purvo
                                            # posledniq arg za -1 kazva obraten red
        newstr = newstr + input[i]
    return newstr

def flipstringrec(string : str):
    char = string[0]
    if len(string) == 1:
        return char
    string = string[1:] #slicevame masiva i ostavqme vsichko osven purviq index
    return flipstringrec(string) + char # sushtata logika kato minalata rec

#originalno se oburkah che trqbva zbor tuiche ostavqm hubav bonus :)

def fib(n):
    nums = [0,0] 
    sum = 0
    for i in range(n - 1): #ako iskame samo purvoto se vrushta defaul sum = 0
        zbor = max(1,nums[0] + nums[1]) # vzimame sbor na posl dve koito e minimum 1 (max(1,)), zashtoto sme 
                                        #preminali purvoto chislo na fib
        sum += zbor #dobavqme kum suma
        nums[0] = nums[1] #izmestvame susednoto predishno v purviq slot
        nums[1] = zbor #slagame novoto vuv vtoriq

    return nums[1], sum #vrushtame n-to chislo i suma, zashtoto ne boli

def fibrec(n): 
    if n == 1: #purvoto chislo na fib si e nula nqma kvo da se smqta
        return 0
    if n == 2: # vtoroto ni e edno i prosto pak si hardcodevame che index 2 == 1, a za ostanalite si raboti -1, ili -2
        return 1
    return fibrec(n - 1) + fibrec(n - 2)

    



print(sum([1,2,3,4,5,6]))
print(sumrec([1,2,3,4,5,6]))
print(flipstring("hello"))
print(flipstringrec("hello"))
#vrushta tuple
result = fib(6)
print(f"Nto chislo na fib index 6 : {result[0]}, sbor do tova chislo : {result[1]}")
print(f"Nto chislo na fib index 6: {fibrec(6)}")