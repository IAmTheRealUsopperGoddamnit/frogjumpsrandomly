def calculate_frog_expected_time():
    # Initial Configuration 
    # We map position -> probability.
    # The frog starts at any integer 0-999 with equal probability (1/1000).
    current_positions = {i: 1/1000.0 for i in range(1000)}
    
    expected_time = 0.0
    probability_finished = 0.0
    
    # We iterate through time steps k = 1, 2, 3...
    # The loop continues until the probability of remaining active is negligible.
    for k in range(1, 100): 
        next_positions = {}
        
        # Calculate jump distance for the k-th jump: 2^(k+1) 
        jump_distance = 2 ** (k + 1)
        
        prob_finished_this_step = 0.0
        
        # Process every position currently occupied by the frog [cite: 13]
        for x, prob in current_positions.items():
            # The recursion logic: 1/2 goes Left, 1/2 goes Right
            # Logic: v_t derived from v_{t+1} logic in Source 13
            
            # Left Move
            left_pos = x - jump_distance
            # Constraint: Frog never jumps to the left of 0 
            if left_pos < 0:
                left_pos = 0
            
            # Right Move
            right_pos = x + jump_distance
            
            # Distribute Probability (0.5 to left, 0.5 to right)
            
            # Check Left Outcome
            next_positions[left_pos] = next_positions.get(left_pos, 0.0) + (0.5 * prob)
                
            # Check Right Outcome
            if right_pos >= 1000:
                prob_finished_this_step += 0.5 * prob
            else:
                next_positions[right_pos] = next_positions.get(right_pos, 0.0) + (0.5 * prob)

        # Update Expected Time Calculation
        # E[T] = Sum(t * Probability(finish at t))
        expected_time += k * prob_finished_this_step
        probability_finished += prob_finished_this_step
        
        # Update positions for the next recursive step
        current_positions = next_positions
        
        # Optimization: If almost all probability mass has finished, stop.
        if probability_finished > 0.9999999:
            break
            
    return expected_time

# Run the calculation
result = calculate_frog_expected_time()
print(f"The Expected Time for the frog to cross the wall is: {result:.4f}")
