# 1-mashq
def merge_sorted_arrays(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

print(merge_sorted_arrays([1,3,5], [2,4,6,8]))
# 2-mashq
def count_vowels_consonants(text):
    vowels = set('aeiouAEIOU')
    v_count = c_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

print(count_vowels_consonants("Python Programming"))
# 3-mashq
def flatten_list(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

print(flatten_list([1, [2, [3, 4], 5], 6, [7, 8]]))
