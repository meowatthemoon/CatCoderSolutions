def solve(length, iterations):
    # Base case: if no more iterations, return the current length
    if iterations == 0:
        return length
    
    # Calculate the length of each smaller segment
    child_length = length / 3
    
    # Recursive perimeter for each iteration (5 segments per previous segment)
    return 5 * solve(child_length, iterations - 1)

if __name__ == '__main__':
    raw_input = input("Input: ")
    raw_input = raw_input.split(" ")
    length = int(raw_input[1].split("=")[1])
    iterations = int(raw_input[2].split("=")[1])

    # Square has 4 segments
    output = 4 * solve(length, iterations) 
    print(output)
