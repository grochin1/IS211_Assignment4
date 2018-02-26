# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from timeit import default_timer as timer

def sequential_search(alist, item):
    start = timer()
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    end = timer()
    return (found, end-start)

def ordered_sequential_search(alist, item):
    start = timer()
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1
    end = timer()
    return (found, end-start)

def binary_search_iterative(alist, item):
    start = timer()
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint
    end = timer()
    return (found, end-start)

def binary_search_recursive(alist, item):
    def binarySearch(_alist, _item):
        if len(_alist) == 0:
            return False
        else:
            midpoint = len(_alist)//2
            if _alist[midpoint]==_item:
                return True
            else:
                if _item<_alist[midpoint]:
                    return binarySearch(_alist[:midpoint],_item)
                else:
                    return binarySearch(_alist[midpoint+1:],_item)
    start = timer()
    found = binarySearch(alist, item)
    end = timer()
    return (found, end-start)

def runtime(size, num):
    print 'size={:d} trials={:d}'.format(size, num)
    times = {'Sequential Search': 0.0, 'Ordered Sequential Search': 0.0,
    'Binary Recursive Search': 0.0, 'Binary Iterative Search':0.0}
    for _ in range(num):
        alist = [random.randint(0, size) for i in range(size)]
        times['Sequential Search'] += sequential_search(alist, -1)[1]
        times['Ordered Sequential Search'] += ordered_sequential_search(alist, -1)[1]
        times['Binary Recursive Search'] += binary_search_recursive(sorted(alist), -1)[1]
        times['Binary Iterative Search'] += binary_search_iterative(sorted(alist), -1)[1]
    for k in times.iterkeys():
        times[k] /= num
        print '%s took %10.7f seconds to run on average'%(k, times[k])
    print '-'*20
    return times

def main():
    rtimes = [
        runtime(500, 100),
        runtime(1000, 100),
        runtime(10000, 100),
    ]
    print 'Average runtimes over sizes 500, 1000 and 10000:'
    avg = {k:0.0 for k in rtimes[0].iterkeys()}
    for r in rtimes:
        for k, v in r.iteritems():
            avg[k] += v
    for k in avg.iterkeys():
        avg[k] /= len(rtimes)
        print '{}: {}'.format(k, str(avg[k]))

if __name__ == '__main__':
    main()
