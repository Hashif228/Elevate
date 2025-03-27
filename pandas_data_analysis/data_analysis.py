def sum_of_evens(nums):
    total=sum(num for num in nums if num % 2 == 0)

    return total

nums = [1, 2, 3, 4, 5, 6]
print(sum_of_evens(nums))  

############################palind  and reverse
def is_palindrome(s):
    ss =s[::-1]
    return ss

print(is_palindrome("hashif"))  

################################prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print('l')
            return False  
    else:
        print('k')
        return True 

print(is_prime(9))  

#############bubble
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))

##linked
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
