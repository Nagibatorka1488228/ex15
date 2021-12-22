def max_pair(arr):
    id_mx = 0
    id_mn = 0
    for i in range(len(arr)):
        if arr[i] > arr[id_mx]:
            id_mx = i
    for j in range(len(arr)):
        if arr[j] < arr[id_mn] and j != id_mx:
            id_mn = j
    arr_new = [arr[id_mn] + arr[id_mx]]
    used = [False] * len(arr)
    used[id_mx] = True
    used[id_mn] = True
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if not used[i] and not used[j]:
                arr_new.append(arr[i] + arr[j])
                used[i] = True
                used[j] = True
                break
    print(arr_new)
    return arr[id_mn] + arr[id_mx]


arr = list(map(int, input().split()))
print(max_pair(arr))
