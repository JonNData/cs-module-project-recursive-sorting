"""
Count how many time "st" occurs in input
Case matters
Use Recursion
"""
def count_st(word):
    # Base case
        # if there is a string less than 2 it can't be a match
    if len(word) < 2:
        return 0
    else:
    # recursive case
        if word[:2] == "st":
            return 1 + count_st(word[2:])
        else:
            return 0 + count_st(word[1:])

print(count_st("ssssStstsststststsststts"))