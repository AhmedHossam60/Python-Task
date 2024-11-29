steps = input("Enter the steps taken each day in a month (space-separated): ").split()
steps = [int(step) for step in steps]

max_steps = max(steps)
min_steps = min(steps)

average_steps = sum(steps) / len(steps)

sorted_steps = sorted(steps, reverse=True)

print("Highest step count:", max_steps)
print("Lowest step count:", min_steps)
print("Average step count: {:.2f}".format(average_steps))
print("Step counts in descending order:", sorted_steps)
