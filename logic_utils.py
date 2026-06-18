def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 10
    return 1, 100

def parse_guess(raw: str):
    try:
        return True, int(raw), None
    except ValueError:
        return False, None, "Please enter a valid number."

def check_guess(guess, secret):
    guess = int(guess)
    if guess == secret:
        return "Win", "Correct!"
    elif guess > secret:
        return "Too High", "Go LOWER"
    else:
        return "Too Low", "Go HIGHER"

def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        return current_score + (10 - attempt_number)
    return current_score
