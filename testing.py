
import os
import list_generator as gen

import time

from file_read_backwards import FileReadBackwards




def backwards(file):
    with FileReadBackwards(file) as frb:

        # getting lines by lines starting from the last line up to get the last sorted
        # if it is not sorted, it means that the algorithm took over 200 sec and it was killed
        #and we wont include it in the next
        

        for line in frb:
            if len(line.split(','))<10:
                continue
            break


        
        return line

        # ok=0
        # kk=0
        # for line in frb:
        #     if line=="" or line=="\n":
        #         k+=1
        #         continue
        #     else:
        #         print("WW",k,line)
        #         line=line.split(",")
        #         if line[10]=="False":
        #             delend("statistics0.csv")
#         #             break
            
#         #     break 





#sort.bucketsort is just for numbers from 0 to 1
auto={0:"sort.bucketsort", 1:"sort.bucketsort2", 2:"sort.bubblesort",3:"sort.selectionsort",4:"sort.insertionsort",\
5:"sort.countingsort", 6:"sort.mergesort",7:"sort.heapsort", 8:"sort.radixsort", 9:"sort.quicksort", 10:"sort.quicksortleft", 11:"sort.quicksortmid", 12:"sort.quicksortright" }

#here can be selected which sorting algorithms to be used
autofreq={0:1, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,12:0 }

def getkey(value):
    for key in auto:
        if auto[key]==value:
            return key


print(getkey(auto[1]))

autogen={0:"gen.basicgenerator",1:"gen.almostsorted",2:"gen.sortedlist",3:"gen.reversesorted",4:"gen.repetitive",5:"gen.floatlist", 6:"gen.subunitarylist" }


generator=gen.basicgenerator
letter='A'

#number of numbers sorted
nr=1

#max value
maxx=10

#min value
minn=0


filename=""

##############
#############




#pystr will be the strig calling the actual python program  




call=["" for x in range(7)]#7 generators (including subunitary el)
for j in range(6,7): #going through the generators

    nr=1
    maxx=10


    generator=autogen[j]

    pystr="python main.py "

    # pystr+=generator 
    # pystr+=' ' 
    call[0]=""
    call[0]+=generator
    call[0]+=" "

    for key in autofreq:
        autofreq[key]=1
    
    if autogen[j]!="gen.subunitarylist":
        autofreq[getkey("sort.bucketsort")]=0
    
    else: #means we are at the last generator: the subunitary one
        autofreq[getkey("sort.bucketsort2")]=0
        autofreq[getkey("sort.countingsort")]=0
        autofreq[getkey("sort.radixsort")]=0
        autofreq[getkey("sort.bucketsort")]=0




    for k in range(7):


        nr*=10
        maxx*=10
        letter=chr(ord('A') + j)
        
        if k>=3 :
            autofreq[getkey("sort.bucketsort2")]=0
            autofreq[getkey("sort.bubblesort")]=0
            autofreq[getkey("sort.selectionsort")]=0
            autofreq[getkey("sort.insertionsort")]=0
            time.sleep(30)

        filename=letter
        filename+=str(k)
        filename+=" "
        #pystr+=filename
        call[1]=""
        call[1]+=filename
        #call[1]+=" "



        for i in range(13):#going through each sorting alg, creating a new process
            
            

            #pystr="python main.py "
            """
            for j in range(11):
                pystr=pystr+str(autofreq[i])+","
            pystr=pystr[:-1] #to eliminate last comma

            pystr+=" "
            """

            if autofreq[i]:
                #pystr+=auto[i]+" "
                call[2]=""
                call[2]+=auto[i]+" "

            else:
                continue


            #pystr+="gen."+generator.__name__+" "

            
            #pystr+=str(nr)+" "
            call[3]=str(nr)+" "


            #pystr+=str(maxx)+" "
            call[4]=str(maxx)+" "


            #pystr+=str(minn)+" "
            call[5]=str(minn)+" "


            ##pystr+=filename

            pystr="python main.py "
            for elem in call:
                pystr+=elem

            print("Operation:",pystr,"\n")

            print(call)
            os.system(pystr)




            lastline=backwards('statistics0.csv').split(',') #we get the last line 
            print("sort."+lastline[2],"-> ",call[2][:-1],'\n')

            if "sort."+lastline[2]!=call[2][:-1] or float(lastline[3])>40:
                autofreq[getkey(call[2][:-1])]=0

            

                        

                    




print("\n\n\n\n\n\n/n/n/n/n/n/n/n")
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################



call=["" for x in range(6)]#6 generators (excluding subunitary el, because we took it above, and it cannot have big numbers)
for j in range(1,6): #going through the generators

    #ok=0#for increasing nr 
    nr=1
    maxx=1000000000#max will be 10 mil all the time


    generator=autogen[j]

    pystr="python main.py "

    # pystr+=generator
    # pystr+=' '
    call[0]=""
    call[0]+=generator
    call[0]+=" "

    for key in autofreq:
        autofreq[key]=1


    autofreq[getkey("sort.bucketsort2")]=0
    autofreq[getkey("sort.countingsort")]=0

    if autogen[j]!="gen.subunitarylist":
        autofreq[getkey("sort.bucketsort")]=0
    
    else: #means we are at the last generator: the subunitary one
        autofreq[getkey("sort.bucketsort2")]=0
        autofreq[getkey("sort.countingsort")]=0
        autofreq[getkey("sort.radixsort")]=0
        autofreq[getkey("sort.bucketsort")]=0



    for k in range(6):
        
        nr*=10
        letter=chr(ord('U') + j)
        
        if k>=3 :
            autofreq[getkey("sort.bucketsort2")]=0
            autofreq[getkey("sort.bubblesort")]=0
            autofreq[getkey("sort.selectionsort")]=0
            autofreq[getkey("sort.insertionsort")]=0
            time.sleep(30)

        filename=letter
        filename+=str(k)
        filename+=" "
        #pystr+=filename
        call[1]=""
        call[1]+=filename
        #call[1]+=" "
    

    
        for i in range(10):#going through each sorting alg, creating a new process
            
            

            #pystr="python main.py "

            if autofreq[i]:
                #pystr+=auto[i]+" "
                call[2]=""
                call[2]+=auto[i]+" "

            else:
                continue


            #pystr+="gen."+generator.__name__+" "

            
            #pystr+=str(nr)+" "
            call[3]=str(nr)+" "


            #pystr+=str(maxx)+" "
            call[4]=str(maxx)+" "


            #pystr+=str(minn)+" "
            call[5]=str(minn)+" "


            ##pystr+=filename

            
            pystr="python main.py "
            for elem in call:
                pystr+=elem

            print(pystr,"\n")


            os.system(pystr)

            lastline=backwards('statistics0.csv').split(',') #we get the last line 
            print("sort."+lastline[2],"-> ",call[2][:-1],'\n')

            if "sort."+lastline[2]!=call[2][:-1] or float(lastline[3])>40:
                autofreq[getkey(call[2][:-1])]=0





