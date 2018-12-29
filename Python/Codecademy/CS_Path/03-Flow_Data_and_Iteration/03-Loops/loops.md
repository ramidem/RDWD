# Loops

- _for loops_ moves through each item in a list.
- _while loops_ keep going until a condition is met.
- _list comprehension_ create new lists

## For Loops

Iterates through the items in a list.

```python
dog_breeds = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

# For Loop
for breed in dog_breeds:
  print(breed)

# Range in For Loop
promise = "I will not chew gum in class"

for i in range(6):
  print(promise)

# Infinite Loops
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  # Changing this to students_period_A will make infinite loop
  students_period_B.append(student)
  print(student)

print(sorted(students_period_B))

# Breaks prevent Infinite Loops
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'

for dog in dog_breeds_available_for_adoption:
  print(dog)
  if dog == dog_breed_I_want:
    print("They have the dog I want!")
    break

# Continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  print(age)
```

## While Loops

The while loop performs a set of code until some condition is reached.

```python
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

count = 0
while count < 6:
  student = all_students.pop()
  students_in_poetry.append(student)
  print(students_in_poetry)
  count += 1

```
