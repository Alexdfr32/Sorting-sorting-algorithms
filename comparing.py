

lst=[]

with open("statistics0.csv","r") as fhand:

    for line in fhand:
        line=line.split(",")
        if len(line)>2:
            lst.append(line)

lst=lst[1:]


###total average time/ total average memory 
###divided into 0-2 and 3-5


#0-2
sortsmall={"bucketsort2":[0,0,0,0],"bubblesort":[0,0,0,0],"selectionsort":[0,0,0,0],"insertionsort":[0,0,0,0],\
"countingsort":[0,0,0,0],"mergesort":[0,0,0,0],"heapsort":[0,0,0,0],"radixsort":[0,0,0,0], "quicksort":[0,0,0,0], "quicksortleft":[0,0,0,0],"quicksortmid":[0,0,0,0],"quicksortright":[0,0,0,0] }


sortbig={"bucketsort2":[0,0,0,0],"bubblesort":[0,0,0,0],"selectionsort":[0,0,0,0],"insertionsort":[0,0,0,0],\
"countingsort":[0,0,0,0],"mergesort":[0,0,0,0],"heapsort":[0,0,0,0],"radixsort":[0,0,0,0], "quicksort":[0,0,0,0], "quicksortleft":[0,0,0,0],"quicksortmid":[0,0,0,0],"quicksortright":[0,0,0,0] }

#[0,0,0,0]
#0,1,2,3 -> 0 for time sum, 1-> for time count , 2->for mem sum 3->mem count


for line in lst:
    if line[0]=='END':
        break
    
    if int(line[0][1:])<3:
        sortsmall[line[2]][0]+=float(line[3])
        #sortsmall[line[2]][1]+=float(line[7])
        sortsmall[line[2]][1]+=1

        sortsmall[line[2]][2]+=float(line[4])
        #sortsmall[line[2]][3]+=float(line[7])
        sortsmall[line[2]][3]+=1
    else:
        sortbig[line[2]][0]+=float(line[3])
        #sortbig[line[2]][1]+=float(line[7])
        sortbig[line[2]][1]+=1

        sortbig[line[2]][2]+=float(line[4])
        #sortbig[line[2]][3]+=float(line[7])
        sortbig[line[2]][1]+=1




try:
    for d in sortsmall:
        sortsmall[d][0]=sortsmall[d][1]/sortsmall[d][0]#numbers per second
        sortsmall[d][1]=sortsmall[d][3]/sortsmall[d][2]#numbers per mb
        # sortsmall[d][0]=sortsmall[d][0]/sortsmall[d][1]#avwerage
        # sortsmall[d][1]=sortsmall[d][2]/sortsmall[d][3]#average

    print("QQQ",sortsmall,"QQQ")

    print()
    print()
    print()
    print()
    # print("YYY",sortbig,"YYY")
    # print()
    # print()

    for d in sortbig:
        sortbig[d][0]=sortbig[d][1]/sortbig[d][0]
        sortbig[d][1]=sortbig[d][3]/sortbig[d][2]
        # sortbig[d][0]=sortbig[d][0]/sortbig[d][1]
        # sortbig[d][1]=sortbig[d][2]/sortbig[d][3]

except:
    print("There's a problem with the Dictionaries.")
    pass

print("YYY",sortbig,"YYY")















mem=[]

with open("statistcsTIME.csv","r") as fhand:

    for line in fhand:
        line=line.split(",")
        if len(line)>2:
            mem.append(line)



mem=mem[1:]

membig=[0,0,0,0]
memsmall=[0,0,0,0]
for line in mem:
    if line[0]=='END' or line[0][-1:]=='':
        break
    

    if int(line[0][-1:])<3:
        memsmall[0]+=float(line[3])
        memsmall[1]+=1

        memsmall[2]+=float(line[4])
        memsmall[3]+=1

    else:
        membig[0]+=float(line[3])
        membig[1]+=1
        membig[2]+=float(line[4])
        membig[3]+=1





membig[0]=membig[0]/membig[1]
membig[1]=membig[2]/membig[3]

print("\n\n\n\n/n/n/n/n",membig, memsmall)





mem=[]

with open("statisticsMEMORY.csv","r") as fhand:

    for line in fhand:
        line=line.split(",")
        if len(line)>2:
            mem.append(line)



mem=mem[1:]

membig=[0,0,0,0]
memsmall=[0,0,0,0]
for line in mem:
    if line[0]=='END' or line[0][-1:]=='':
        break
    

    if int(line[0][-1:])<3:
        memsmall[0]+=float(line[3])
        memsmall[1]+=1

        memsmall[2]+=float(line[4])
        memsmall[3]+=1

    else:
        membig[0]+=float(line[3])
        membig[1]+=1
        membig[2]+=float(line[4])
        membig[3]+=1





membig[0]=membig[0]/membig[1]
membig[1]=membig[2]/membig[3]

print("\n\n\n\n/n/n/n/n",membig, memsmall)




