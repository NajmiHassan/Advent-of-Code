def mix_number(secret, value):
    """Mix a value into the secret number using XOR."""
    return secret ^ value

def prune_number(secret):
    """Prune the secret number using modulo."""
    return secret % 16777216

def generate_next_secret(secret):
    """Generate the next secret number in the sequence."""
    # Step 1: Multiply by 64 and mix
    result = mix_number(secret, secret * 64)
    result = prune_number(result)
    
    # Step 2: Divide by 32 and mix
    result = mix_number(result, result // 32)
    result = prune_number(result)
    
    # Step 3: Multiply by 2048 and mix
    result = mix_number(result, result * 2048)
    result = prune_number(result)
    
    return result

def generate_nth_secret(initial_secret, n):
    """Generate the nth new secret number in the sequence."""
    current = initial_secret
    for _ in range(n):
        current = generate_next_secret(current)
    return current

def solve_puzzle(input_data):
    # Parse input
    initial_secrets = [int(line.strip()) for line in input_data.strip().split('\n')]
    
    # Generate 2000th secret for each initial secret
    secrets_2000 = [generate_nth_secret(secret, 2000) for secret in initial_secrets]
    
    # Return sum of 2000th secrets
    return sum(secrets_2000)

# your puzzle input
example_input = """
13705650
3590521
13848854
4951006
1021840
"""

# Verify with example
result = solve_puzzle(example_input)
print(f"Example result: {result}")  # Should be 37327623

# You can now use this with your actual puzzle input
# actual_input = '''your puzzle input here'''
# result = solve_puzzle(actual_input)
# print(f"Puzzle result: {result}")