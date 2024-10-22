def bucket_sort(my_list):
    n = len(my_list)
    buckets = [[]for _ in range(n)]
    for num in  my_list:
        index = int(num*n)
        buckets[index].append(num)
    for bucket in buckets:
        bucket.sort()
    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(bucket)
    return sorted_list
arr = [0.8, 0.2, 0.4, 0.6, 0.1, 0.9, 0.3, 0.7, 0.5]
print(bucket_sort(arr))
