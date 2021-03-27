lst = [
    (3,"Fizz"),
    (5,"Buzz")
]

for i in range(1,101):
    output = ""
    for x in lst:
        if i%x[0] == 0: output += x[1]
    if output == "": output = i
    
    print(output)