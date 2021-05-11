import numpy as np
import time
import timeit
import pickle
import csv
import random as rand
import sort
import list_generator as gen
import tracemalloc
import re
import multiprocessing
import gc
import sys
from memory_profiler import memory_usage
import line_profiler
from guppy import hpy
import statistics
import signal
#https://docs.python.org/3/library/tracemalloc.html

import sys












def main(onegenerator, filename, onesortalg, nr, maxx, minn):

  a=''#the array actually sorted
  ssort=eval(onesortalg)
  g=eval(onegenerator)
  f=ssort#sortingalg

  nr=int(nr)
  maxx=int(maxx)
  minn=int(minn)



  try:
    with open(filename,'r') as fi:
      reader=csv.reader(fi)
      a=list(reader)
      a=list(map(int, a[0]))

  except:
    with open(filename,'w') as fi:
      writer=csv.writer(fi)
      a=g(minn,maxx,nr)
      writer.writerow(a)
    first=0





  try:
    with open(filename,'r') as fi:
      reader=csv.reader(fi)
      a=list(reader)
      a=list(map(int, a[0]))

  except:
    with open(filename,'w') as fi:
      writer=csv.writer(fi)
      a=g(minn,maxx,nr)
      writer.writerow(a)
    first=0

  i=6 #change
  f=ssort


  start=time.time()

  notkilled=1
  try:
    if ssort==sort.quicksort or ssort==sort.quicksortleft or ssort==sort.quicksortmid or ssort==sort.quicksortright:
      left=0
      right=len(a)-1
      b=(a,left,right)
      mem=memory_usage((ssort,b))

    else:
      if ssort==sort.bucketsort2 or ssort==sort.countingsort:
        b=(a,minn,maxx)
        mem=memory_usage((ssort,b))

      else:
        b=(a,)
        mem=memory_usage((ssort,b))
  
  except:
    mem=[0]
    notkilled=0
    



  end=time.time()

  print("average memory in MB:",sum(mem)/len(mem))




  memmin=min(mem)
  memmax=max(mem)
  memmin=mem[0]
  memmax=mem[0]
  for elem in mem:
    if elem>memmin:
      memmin=elem
    if elem<memmin:
      memmax=elem 



  mem=(sum(mem)/len(mem))






  print(filename)
  print(g.__name__)
  print("Algorithm     ",f.__name__)
  print("time:      ",float(end-start),"sec")





  print("Average memory size      ",str(mem))   
  
  print("Min memory size      ",str(memmax))

  print("Max memory size      ",str(memmin))

  print("numbers sorted    ",nr)
  print("min value      ",minn)
  print("max val     ",maxx)


  print("is sorted:    ", sort.issorted(a))

  if notkilled:
    #fields=['Csv name','Generator','Algorithm','Time','Averge Memory','Max memory', 'Min memory','Numbers sorted','Min Val','Max Val','Issorted']
    fields=[filename, g.__name__, f.__name__, float(end-start),mem,memmax,memmin, nr,minn,maxx,sort.issorted(a) ]
    with open('statisticsnew.csv', 'a') as ff:
        writer = csv.writer(ff)
        writer.writerow(fields)
  






if __name__=="__main__":
  main(sys.argv[1], sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])


