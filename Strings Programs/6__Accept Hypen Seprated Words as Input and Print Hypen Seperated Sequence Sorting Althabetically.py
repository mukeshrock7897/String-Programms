print("Enter The Hypen Seperated Words::")
a=[i for i in input().split('-')]
a.sort()
print("Sorted String::")
print('-'.join(a))
