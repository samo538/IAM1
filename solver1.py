# Function that finds the super divisor of a given number
def super_divisor(n):
    if (n == 1 or n == 0):
        return 0

    # Fills the candidates array with all divisors
    candidates = []
    for i in range(1,n):
        if (n % i == 0):
            candidates.append(i)

    # Returns the last divisor (and the largest one)
    return candidates[-1]


def find_solutions(goal):
    solutions = []

    # The solutions must be lesser that goal
    for i in range(2,goal + 1):
        total_sum = 0
        current_value = i

        # Sum until super_divisor == 0
        while (total_sum <= goal):
            total_sum += current_value
            current_value = super_divisor(current_value)

            if (current_value == 0):
                break

        # If the total_sum == goal, we have found a solution
        if (total_sum == goal):
            solutions.append(i)

    # Return solutions
    return solutions

# Sets the goal
goal = 2025
# Prints all of the solutions
print(find_solutions(goal))
