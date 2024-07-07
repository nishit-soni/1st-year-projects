import numpy as np
import matplotlib.pyplot as plt

# AND gate inputs and outputs
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([0, 1, 1, 1])

# Initialize weights and bias
weights = np.zeros(2)
bias = 0

# Training loop
while True:
    converged = True  # Assume convergence until proven otherwise
    for i in np.random.permutation(len(inputs)):  # Randomly pick a point
        input_vector = inputs[i]
        expected_output = outputs[i]
        
        # Calculate the perceptron output
        perceptron_output = 1 if np.dot(input_vector, weights) + bias > 0 else 0
        
        # Update rule
        if expected_output == 1 and perceptron_output == 0:
            weights += input_vector
            bias += 1
            converged = False
        elif expected_output == 0 and perceptron_output == 1:
            weights -= input_vector
            bias -= 1
            converged = False
            
    if converged:
        break

print("Weights:", weights)
print("Bias:", bias)

# Plotting
plt.figure()

# Plot the points
plt.scatter(inputs[:, 0], inputs[:, 1], c=outputs, cmap='coolwarm', s=100, edgecolors='k')

# Plot the decision boundary if the second weight is not zero
if weights[1] != 0:
    x_vals = np.array([0, 1])
    y_vals = -(weights[0] * x_vals + bias) / weights[1]
    plt.plot(x_vals, y_vals, 'k--')  # Decision boundary

plt.xlabel('Input 1')
plt.ylabel('Input 2')
plt.title('Perceptron Decision Boundary for AND Gate')
plt.grid(True)
plt.show()
