# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from timeit import default_timer as timer

def insertion_sort(alist):
    start = timer()
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
        alist[position]=currentvalue
    return timer()-start

def shell_sort(alist):
    def gapInsertionSort(alist_,start_,gap_):
        for i in range(start_+gap_,len(alist_),gap_):
            currentvalue = alist_[i]
            position = i
            while position>=gap_ and alist_[position-gap_]>currentvalue:
                alist_[position]=alist_[position-gap_]
                position = position-gap_
            alist_[position]=currentvalue

    start = timer()
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2
    return timer()-start

def python_sort(alist):
    start = timer()
    alist.sort()
    return timer()-start

def runtime(size, num):
    print 'size={:d} trials={:d}'.format(size, num)
    times = {
        'Insertion Sort': 0.0, 'Shell Sort': 0.0,
        'Python Sort': 0.0
    }
    for _ in range(num):
        alist = [random.randint(0, size) for i in range(size)]
        times['Insertion Sort'] += insertion_sort(alist)
        times['Shell Sort'] += shell_sort(alist)
        times['Python Sort'] += python_sort(alist)
    for k in times.iterkeys():
        times[k] /= num
        print '%s took %10.7f seconds to run on average'%(k, times[k])
    print '-'*20
    return times

def main():
    rtimes = [
        runtime(500, 100),
        runtime(1000, 100),
        runtime(10000, 100), # this takes a long time!
    ]
    print 'Average runtime over all sizes:'
    avg = {k:0.0 for k in rtimes[0].iterkeys()}
    for r in rtimes:
        for k, v in r.iteritems():
            avg[k] += v
    for k in avg.iterkeys():
        avg[k] /= len(rtimes)
        print '%s took %10.7f seconds to run on average'%(k, avg[k])

if __name__ == '__main__':
    main()
