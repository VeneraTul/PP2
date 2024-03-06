with open("ex.txt","r") as rf:
    with open("ex_copy","w") as wf:
        for line in rf:
            wf.write(line)