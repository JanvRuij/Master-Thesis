def generate_sequence(N):
    sequence = []
    num = 1
    while len(sequence) < N:
        for i in range(3):
            sequence.extend([num, num + 1])
        num += 4
        print(sequence)
    return sequence[:N]

# Example usage:
N = 4
result_sequence = generate_sequence(N)
for num in result_sequence:
    print(num, num + 2)
