## Tuples

# Create tuple and print elements

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

for t in tup:
    print(t)


# Find the length of tuple
def length(tup):
    return len(tup)

print(length(tup))


## Sets

## Function to check prime
def check_prime(n):
    if n == 0 or n == 1:
        print("Neither Prime nor Composite")
    
    for i in range(2, n):
        if n % i != 0:
            return "Not Prime"
        else:
            return "Prime"
    else:
        return "Prime"


s1 = {i for i in range(1, 50) if check_prime(i)}
s2 = {i for i in range(1, 50, 2)}

print("Prime num: ", s1)
print("Odd num: ", s2)

print("Intersection of two sets: ", s1.intersection(s2))


## Union of sets
# print(s1.union(s2))

## Check subset
print(s2.issubset(s1))
