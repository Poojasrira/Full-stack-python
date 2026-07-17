lines = []

def read_lines():
    global lines
    with open("poem.txt", "r") as f:
        lines = f.readlines()

def clean():
    import re
    global lines
    pat=r"[^A-Za-z0-9 ]"
    lines = list(map(lambda line:re.sub(pat,"",line), lines))

def print_lines():
    for line in lines:
        print(line) 

read_lines()
clean()
print_lines()