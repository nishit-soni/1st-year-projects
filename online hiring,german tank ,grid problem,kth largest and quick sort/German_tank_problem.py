import random

def german_tank_problem(k, n):
    # Draw k samples from range 1 to n with replacement
    samples = random.choices(range(1, n+1), k=k)
    m = max(samples)  # Maximum observed number in the samples
    # Apply the German Tank Problem formula for estimation
    estimated_max = (m * (k + 1) / k) - 1
    return estimated_max

# Input from the user
n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k: "))

# Print the estimated maximum based on the sample
print(german_tank_problem(k, n))



