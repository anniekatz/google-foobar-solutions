'''
* Find the terminal states in the matrix. All their transition probabilities are 0.
* Find the non-terminal states in the matrix. These states have at least one possible transition to another state.
* Set the self-transition probabilities (probability of transitioning from a state to itself) to 0.
* Multiplying the transition probabilities of the non-terminal states into matrix
* Total probability = sum of the probabilities of reaching the terminal states.
* If the total probability is 0, set all probabilities of reaching the terminal states to 1 and set the total probability to the num of terminal states.
* Return the list of numerators for the probabilities of reaching the terminal states, then the denominator as the total probability.
'''

def solution(matrix):
    # Find the terminal states
    term_states = []
    for i, row in enumerate(matrix):
        # Check if all elements in row are 0
        if all(x == 0 for x in row):
            # If all elements are 0, append the index to term_states
            term_states.append(i)

    # Find the non-terminal states
    nonterm_states = list(set(range(len(matrix))) - set(term_states))

    # Set the prob of a transition to self to 0
    for i, row in enumerate(matrix):
        # Set the element at the current index to 0
        matrix[i][i] = 0

    # Multiply the non-terminal states into one matrix
    for i in range(len(nonterm_states) - 1):
        index1 = nonterm_states[len(nonterm_states) - i - 1]
        for j in range(len(nonterm_states) - 1):
            index2 = nonterm_states[j]
            # Multiply the probabilities of the two non-terminal states
            matrix[index2] = multiply_nt_probs(matrix[index2], index2, matrix[index1], index1)

    # Extract the probabilities of reaching the terminal states
    probs_of_term = [matrix[0][i] for i in term_states]

    # Calculate the total probability
    total = sum(probs_of_term)
    if total == 0:
        # If the total probability is 0, set all probabilities to 1
        probs_of_term = [1 for i in term_states]
        total = len(term_states)

    # Generate the output
    output = probs_of_term + [total]
    return output

# Function to multiply the probabilities of transitioning from two
# non-terminal states
def multiply_nt_probs(m1, i1, m2, i2):
    # Get the indices of the states in m1 and m2 that are not i1 or i2
    indices = set(range(len(m1))) - {i1, i2}
    # Calculate the sum of the probabilities in v2
    sum_m2 = sum(m2)
    # Initialize the output list with 0s
    out_list = [0 for i in m1]
    for i in indices:
        # Calculate the probability of transitioning to state i
        # from state i1 and i2
        out_list[i] = sum_m2 * m1[i] + m1[i2] * m2[i]
    # Calculate the greatest common denominator of the probabilities
    gc = gcd_arr(out_list)
    # Divide the probabilities by the greatest common denominator
    prob_output = [int(i / gc) for i in out_list]
    return prob_output


# Greatest common denominator- avoid division by 0
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Function to find the greatest common denominator of a list/array
def gcd_arr(arr):
    gcd_output = 0
    for i in arr:
        gcd_output = gcd(gcd_output, i)
    return gcd_output

