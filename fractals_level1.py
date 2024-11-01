def solve(length, iterations):
    # Base case: if no more iterations, return the current length
    if iterations == 0:
        return length
    
    # Calculate the length of each smaller segment
    child_length = length / 3
    
    # Recursive perimeter for each iteration (4 segments per previous segment)
    return 4 * solve(child_length, iterations - 1)

if __name__ == '__main__':
    raw_input = input("Input: ")
    raw_input = raw_input.split(" ")
    length = int(raw_input[1].split("=")[1])
    iterations = int(raw_input[2].split("=")[1])

    # Triangle has 3 segments
    output = 3 * solve(length, iterations) 
    print(output)
