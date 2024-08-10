def read_input():
    cases = int(input("Please enter the number of cases: "))
    dfa_cases = []
    
    for _ in range(cases):
        n = int(input("Please enter the number of states: "))
        alphabet = input("Please enter the alphabet (space-separated): ").split()
        final_states = list(map(int, input("Please enter the final states (space-separated): ").split()))
        transition_table = []
        
        for i in range(n):
            transitions = list(map(int, input(f"Please enter transitions for state {i}: ").split()))
            transition_table.append(transitions)
        
        dfa_cases.append((n, alphabet, final_states, transition_table))
    
    return dfa_cases

def find_equivalent_states(dfa):
    n, alphabet, final_states, transition_table = dfa
    equivalent_pairs = []
    state_equivalence = {}

    # Initialize state equivalence  
    for state in range(n):
        state_equivalence[state] = set()

    # Check for equivalent states
    for p in range(n):
        for q in range(p + 1, n):
            if are_equivalent(p, q, final_states, transition_table):
                equivalent_pairs.append((p, q))
                state_equivalence[p].add(q)
                state_equivalence[q].add(p)

    return equivalent_pairs

def are_equivalent(p, q, final_states, transition_table, visited=None):
    if visited is None:
        visited = set()
        
    # Create a unique identifier for the state pair
    state_pair = (min(p, q), max(p, q))
    
    # Check if this state pair has already been visited
    if state_pair in visited:
        return True  # Already checked this pair, assume equivalent for now
    
    visited.add(state_pair)

    # Check if both states are final or both are not final
    if (p in final_states) != (q in final_states):
        return False
    
    # Check transitions for each symbol in the alphabet
    for symbol_index in range(len(transition_table[0])):
        next_p = transition_table[p][symbol_index]
        next_q = transition_table[q][symbol_index]
        if not are_equivalent(next_p, next_q, final_states, transition_table, visited):
            return False
            
    return True
 
def main():
    while True:
        print("\nMenu:")
        print("1. Read DFA input")
        print("2. Find equivalent states")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            dfa_cases = read_input()
            print("DFA cases read successfully.")
        
        elif choice == '2':
            if 'dfa_cases' not in locals():
                print("Please read DFA input first.")
                continue
            
            for dfa in dfa_cases:
                equivalents = find_equivalent_states(dfa)
                if equivalents:
                    print("Equivalent states:", ' '.join(f"({p}, {q})" for p, q in equivalents))
                else:
                    print("No equivalent states found.")
        
        elif choice == '3':
            print("Exiting.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
