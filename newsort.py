


import os
import list_generator as gen

import time
start=time.time()


sortal={0:"bucketsort", 1:"bucketsort2", 2:"bubblesort",3:"selectionsort",4:"insertionsort",\
5:"countingsort", 6:"mergesort",7:"heapsort", 8:"radixsort", 9:"quicksort", 10:"quicksortleft", 11:"quicksortmid", 12:"quicksortright" }


#these are the A's
generators={"A":"basicgenerator",'B':"almostsorted",'C':"sortedlist",'D':"reversesorted",'E':"repetitive",'F':"floatlist", 'G':"subunitarylist" }


lst=[]

with open("statistics0.csv","r") as fhand:

    for line in fhand:
        line=line.split(",")
        if len(line)>2:
            lst.append(line)

lst=lst[1:]







table=[[0 for _ in range(6)] for _ in range(13)]

#rows={0:1,1:1,22,33,44,55, }
rows={'A':0,'B':1, 'C':2,  'D':3 ,'E':4, 'F':5, 'G':6  ,\
    'U':7, 'V':8, 'W':9, 'X':10, 'Y':11, 'Z':12}
#IF LETTER>G -> ROW[x+5] 

#print(lst)

j=0
letter='A'


for row in rows:
    

    for i in range(6):
        # print(i)
        # print(lst[j][0],' -> ',str(str(chr(ord(row)))+str(i)))
        while lst[j][0]==str(str(chr(ord(row)))+str(i)):#while we are at the same gen and(+) size
            # print(lst[j][0])
            if table[rows[row]][i]==0:
                table[rows[row]][i]=lst[j][0]
                mintime=float(lst[j][3])
                best=lst[j][2]
            else:
                if float(lst[j][3])<mintime:
                    mintime=float(lst[j][3])
                    best=lst[j][2]


            j+=1
            if lst[j][0]=='END':
                break
        
        table[rows[row]][i]=best
        while lst[j][0][1:]=='6': 
            j+=1

    pass


autogen={0:"gen.basicgenerator",1:"gen.almostsorted",2:"gen.sortedlist",3:"gen.reversesorted",4:"gen.repetitive",5:"gen.floatlist", 6:"gen.subunitarylist" }



call=["" for x in range(7)]



call=["" for x in range(7)]


for j in range(0,7):

    nr=1
    maxx=10
    minn=0


    generator=autogen[j]

    pystr="python main.py "


    call[0]=""
    call[0]+=generator
    call[0]+=" "

    for k in range(6):

        nr*=10
        maxx*=10
        letter=chr(ord('A') + j)
        


        filename="TIME_"+letter

        filename+=str(k)
        filename+=" "

        call[1]=""
        call[1]+=filename
        call[1]+=" "
        
        call[2]="sort."+str(table[rows[letter]][k])+" "



        call[3]=str(nr)+" "

        call[4]=str(maxx)+" "

        call[5]=str(minn)+" "



        pystr="python main.py "
        for elem in call:
            pystr+=elem
        print("Operation:",pystr,"\n")
        os.system(pystr)




call=["" for x in range(7)]





for j in range(0,7):

    nr=1
    maxx=1000000000
    minn=0


    generator=autogen[j]

    pystr="python main.py "

    # pystr+=generator 
    # pystr+=' ' 
    call[0]=""
    call[0]+=generator
    call[0]+=" "

    for k in range(6):

        nr*=10
        letter=chr(ord('U') + j)
        


        filename="TIME_"+letter
        #filename=letter
        filename+=str(k)
        filename+=" "
        # #pystr+=filename
        call[1]=""
        call[1]+=filename
        call[1]+=" "
        
        call[2]="sort."+str(table[rows[letter]][k])+" "
        # print(call)


        call[3]=str(nr)+" "

        call[4]=str(maxx)+" "

        call[5]=str(minn)+" "


        # print(call)
        pystr="python main.py "
        for elem in call:
            pystr+=elem
        # print(call)
        print("Operation:",pystr,"\n")
        os.system(pystr)











table2=[[0 for _ in range(6)] for _ in range(13)]

j=0
for row in rows:
    
    # print(row)
    for i in range(6):
        # print(lst[j][0],' -> ',str(str(chr(ord(row)))+str(i)))
        while lst[j][0]==str(str(chr(ord(row)))+str(i)):#while we are at the same gen and(+) size

            if table2[rows[row]][i]==0:
                table2[rows[row]][i]=lst[j][0]
                minmemory=float(lst[j][4])
                best=lst[j][2]
            else:
                if float(lst[j][4])<minmemory:
                    minmemory=float(lst[j][4])
                    best=lst[j][2]

            # table2[rows[row]][i]=best
            # j+=1
            j+=1
            if lst[j][0]=='END':
                break
        table2[rows[row]][i]=best
        while lst[j][0][1:]=='6': 
            j+=1




call=["" for x in range(7)]


for j in range(0,7):

    nr=1
    maxx=10
    minn=0


    generator=autogen[j]

    pystr="python main.py "


    call[0]=""
    call[0]+=generator
    call[0]+=" "

    for k in range(6):

        nr*=10
        maxx*=10
        letter=chr(ord('A') + j)
        


        filename="MEMORY_"+letter

        filename+=str(k)
        filename+=" "

        call[1]=""
        call[1]+=filename
        call[1]+=" "
        
        call[2]="sort."+str(table2[rows[letter]][k])+" "



        call[3]=str(nr)+" "

        call[4]=str(maxx)+" "

        call[5]=str(minn)+" "



        pystr="python main.py "
        for elem in call:
            pystr+=elem
        print("Operation:",pystr,"\n")
        os.system(pystr)




call=["" for x in range(7)]




for j in range(0,7):

    nr=1
    maxx=1000000000
    minn=0


    generator=autogen[j]

    pystr="python main.py "


    call[0]=""
    call[0]+=generator
    call[0]+=" "

    for k in range(6):

        nr*=10
        letter=chr(ord('U') + j)
        


        filename="MEMORY_"+letter

        filename+=str(k)
        filename+=" "

        call[1]=""
        call[1]+=filename
        call[1]+=" "
        
        call[2]="sort."+str(table2[rows[letter]][k])+" "



        call[3]=str(nr)+" "

        call[4]=str(maxx)+" "

        call[5]=str(minn)+" "


        pystr="python main.py "
        for elem in call:
            pystr+=elem

        print("Operation:",pystr,"\n")
        os.system(pystr)








