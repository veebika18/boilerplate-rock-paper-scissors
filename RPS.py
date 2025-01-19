def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    # Default prediction and counter
    if len(opponent_history) < 3:
        return "R"
    
    # Get the last three moves as a pattern
    last_three = "".join(opponent_history[-3:])
    
    # Predict the next move based on patterns
    patterns = {"R": 0, "P": 0, "S": 0}
    for i in range(len(opponent_history) - 3):
        if "".join(opponent_history[i:i + 3]) == last_three:
            next_move = opponent_history[i + 3]
            patterns[next_move] += 1
    
    # Choose the most common predicted move or default to "R"
    predicted_move = max(patterns, key=patterns.get) if patterns else "R"
    
    # Return the counter move
    return {"R": "P", "P": "S", "S": "R"}[predicted_move]
