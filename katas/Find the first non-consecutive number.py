def first_non_consecutive(arr):
    for e,elem in enumerate(arr,arr[0]):
        if e!=elem:
            return elem







print(first_non_consecutive([1,2,3,4,6,7,8]))