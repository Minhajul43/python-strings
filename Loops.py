# Loops in Python

# For loop
for i in range(5):
    print("Iteration:", i)

# While loop
count = 0
while count < 5:
    print("While iteration:", count)
    count += 1

  # Nested loop
for i in range(3):
    for j in range(2):
        print("Nested loop iteration:", i, j)

  # Loop control statements
# Break statement
for i in range(10):
    if i == 5:
        break
    print("Break iteration:", i)

# Continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print("Continue iteration:", i)

    # Pass statement
for i in range(5):
    if i == 3:
        pass
    else:
        print("Pass iteration:", i)

        # Loop with else
for i in range(5):
    print("Loop with else iteration:", i)
else:
    print("Loop with else completed.")

    # do while loop simulation
count = 0
while True:
    print("Do while loop simulation iteration:", count)
    count += 1
    if count >= 5:
        break
    