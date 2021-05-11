import numpy as np
import time
import timeit
import pickle
import csv
import random as rand
import sort
import tracemalloc
#https://docs.python.org/3/library/tracemalloc.html

#import .sort\



def basicgenerator(start,stop,steps):

  #return np.random.randint (start,stop,steps).tolist()
  return [rand.randint(start+1, stop-1) for _ in range(steps)]
  

def almostsorted(start,stop,size):

  st=stop-size-1
  a=[i for i in range(st,stop-1)]

  for i in range(5):
    r=rand.randint(1,size-2)
    a[r],a[r+1]=a[r+i],a[r]
  
  return a


def sortedlist(start,stop,size):
  st=stop-size-1
  return [i for i in range(st,stop-1)]


def reversesorted(start,stop,size):
  st=stop-size-1
  return [i for i in range(st,stop-1)]



def repetitive(start,stop,size):
  st=stop-size-1
  listt=[rand.randint(st, stop) for _ in range(10)]
  return [rand.choice(listt) for _ in range(size)]


def floatlist(start,stop,size):
  return [rand.uniform(start,stop) for _ in range(size)]




def subunitarylist(start,stop,size):#start,stop are here just to have the same template on func arg as above
  return [rand.random() for _ in range(size)]


