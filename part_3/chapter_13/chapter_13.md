Chapter 13 : More Sorting
=========================
In this chapter I implemant merge sort, quick sort and counting sort. Here descibe those sort : 

## Merge Sort

***Program : merge two sorted list***
```python
# merge function -> merge two sorted list
def merge(_list_one:list,_list_two:list)->list:
    len_one = len(_list_one);
    len_two = len(_list_two);
    index_one = 0;
    index_two = 0;

    # merge list
    merged_list = [];

    # start to merging
    while index_one < len_one and index_two < len_two:
        if _list_one[index_one] < _list_two[index_two]:
            merged_list.append(_list_one[index_one]);
            index_one += 1;
        else:
            merged_list.append(_list_two[index_two]);
            index_two += 1;

    if index_one < len_one:
        merged_list += _list_one[index_one:];

    if index_two < len_two:
        merged_list += _list_two[index_two:];

    return merged_list;
```

***Program : merge sort***
```python
# merge sort
def merge_sort(_list:list)->list:
    if len(_list) <= 1:
        return _list;

    mid = len(_list)//2;
    left = merge_sort(_list[:mid]);
    right = merge_sort(_list[mid:]);
    return merge(left,right);
```

## Quick Sort 

***Program : partition***
```python
# swap -> swap two list element by their index
def swap(l:list,ai:int,bi:int)->list:
    l[ai],l[bi] = l[bi],l[ai];
    return l;

# partition
def partition(l:list,low:int=0,high:int=None):
    if high == None : high = len(l) - 1;
    index = low - 1;
    pivot = l[high];

    # place the pivot correct place
    for i in range(low,high):
        if l[i] <= pivot :
            swap(l,index+1,i);
            index += 1;
    
    swap(l,index+1,high);
    return index+1; # return index of pivot

```

***Program : quick sort***
```python
# quick sort
def quick_sort(l:list,low:int=0,high:int=None):
    if high == None :
        high = len(l) -1;
    
    if low >= high : 
        return l;

    # partition whole array first
    pivot_index = partition(l,low,high);
    quick_sort(l,low,pivot_index-1);
    quick_sort(l,pivot_index+1,high);

    return l;
```

## Counting Sort

```python
# counting_sort
def counting_sort(l:list,high:int):
    counting_list = [0]*(high + 1);
    sorted_list = [];

    # counting start 
    for i in l : 
        counting_list[i] += 1;
    
    # create sorted list based on counting list
    for i in range(high+1):
        if counting_list[i]: 
            for j in range(counting_list[i]):
                sorted_list.append(i);
    
    return sorted_list;
```