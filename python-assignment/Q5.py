import myMath
import matplotlib.pyplot as plt


def cos(x):
    # Convert x to radians
    x = x * (3.14159/180)

    # Initialize variables
    result = 1
    term = 1
    i = 2

    # Calculate Maclaurin series
    while abs(term) > 0.0001:
        term = (-1)**i * myMath.pow(x, 2*i) / myMath.factorial(2*i)
        result += term
        i += 1

    return result


# Test the function
print(cos(30))

# Plot the series
x_values = [i for i in range(-360, 361)]
y_values = [cos(x) for x in x_values]

plt.plot(x_values, y_values)
plt.title("Cosine Function using Maclaurin Series")
plt.xlabel("x (degrees)")
plt.ylabel("y = cos(x)")
plt.savefig('McClaurin_Series.png')


plt.show()
