
"""

 a        |  1   |   2   |  3   |  4   | nthsize |
comp      |  0   |   1   |  2   |  3   |  n-1    |
iterations|  0   |   1   |  2   |  2   |  n-1    |

    Time complexity average = O(n^2)
"""


def bubble_sort(a):

    not_sorted = True

    while not_sorted:
        not_sorted = False

        for i in range(1,len(a)):

            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                not_sorted = True

    return a


print(bubble_sort([16, 19, 13, 18, 15]))
print(bubble_sort([0, 1, 2, 3, 4]))
print(bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(bubble_sort([]))
print(bubble_sort([1, 3, 5, 10, 8, 2, 3, 6, 8, 3, 2, 3, 2, 1, 6, 7, 3, 44, 678]))
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
print(bubble_sort([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(bubble_sort([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]))
