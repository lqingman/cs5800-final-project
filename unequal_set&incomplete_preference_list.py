"""
Final project code
Qingman Li
stable matching with incomplete preference lists
and stable matching with ties in preference lists
"""


def stable_matching_unequal_size(men_preferences, women_preferences):
    """
    function to find a stable matching of unequal size of men and women
    """
    # Initially, all men and women are free
    free_men = list(men_preferences.keys())
    # Create an empty dictionary to store engaged pairs
    engaged = {}
    # Keep track of the next woman each man should propose to
    next_proposal = {man: 0 for man in men_preferences}

    # Helper function to check if a woman prefers a new man over her current partner
    def prefers(woman, new_man, current_partner):
        # If the woman has no current partner, she prefers the new man
        if current_partner is None:
            return True
        # Otherwise, check if she prefers the new man over her current partner
        return women_preferences[woman].index(new_man) < women_preferences[woman].index(current_partner)

    # While there is a free man who still has a woman to propose to
    while free_men:

        # Get the next free man
        man = free_men.pop(0)
        man_pref_list = men_preferences[man]

        # Find the next woman this man has not yet proposed to
        while next_proposal[man] < len(man_pref_list):
            woman = man_pref_list[next_proposal[man]]
            next_proposal[man] += 1

            # If the woman is free or prefers this man over her current partner
            current_partner = engaged.get(woman)
            if prefers(woman, man, current_partner):
                if current_partner:
                    free_men.append(current_partner)
                engaged[woman] = man
                break
        # If this man has proposed to all women, he remains unmatched
    return engaged


def stable_matching_incomplete(men_preferences, women_preferences):
    """
    function to find a stable matching of incomplete preference lists
    """
    free_men = list(men_preferences.keys())
    engaged = {}
    next_proposal = {man: 0 for man in men_preferences}

    # Helper function to check if a woman prefers a new man over her current partner
    def prefers(woman, new_man, current_partner):
        # check the acceptability of the man to the woman
        if new_man not in women_preferences[woman]:
            return False
        if current_partner is None:
            return True
        return women_preferences[woman].index(new_man) < women_preferences[woman].index(current_partner)

    while free_men:
        man = free_men.pop(0)
        man_pref_list = men_preferences[man]

        while next_proposal[man] < len(man_pref_list):
            woman = man_pref_list[next_proposal[man]]
            next_proposal[man] += 1

            current_partner = engaged.get(woman)
            if prefers(woman, man, current_partner):
                if current_partner:
                    free_men.append(current_partner)
                engaged[woman] = man
                break
        # If this man has proposed to all women on his list, he remains unmatched

    return engaged


def main():
    # Example 1: Stable Matching with unequal size
    men_preferences1 = {
        'A': ['W3', 'W5', 'W4', 'W2', 'W1'],
        'B': ['W4', 'W3', 'W1', 'W5', 'W2'],
        'C': ['W2', 'W5', 'W1', 'W4', 'W3'],
        'D': ['W5', 'W1', 'W3', 'W2', 'W4'],
        'E': ['W1', 'W2', 'W4', 'W3', 'W5'],
        'F': ['W4', 'W2', 'W5', 'W1', 'W3'],
        'G': ['W3', 'W5', 'W2', 'W4', 'W1']
    }

    women_preferences1 = {
        'W1': ['E', 'D', 'F', 'B', 'A', 'C', 'G'],
        'W2': ['B', 'A', 'F', 'G', 'C', 'D', 'E'],
        'W3': ['G', 'A', 'D', 'C', 'E', 'F', 'B'],
        'W4': ['A', 'C', 'B', 'G', 'E', 'F', 'D'],
        'W5': ['C', 'E', 'D', 'B', 'G', 'F', 'A']
    }

    # Example 2: Stable Matching with incomplete preference lists
    men_preferences2 = {
        'A': ['W1', 'W2', 'W3', 'W4', 'W5'],
        'B': ['W4', 'W2', 'W1', 'W5'],
        'C': ['W3', 'W1', 'W5'],
        'D': ['W2', 'W4', 'W1', 'W3'],
        'E': ['W3', 'W5'],
        'F': ['W2', 'W5', 'W3', 'W1'],
        'G': ['W1', 'W3']
    }

    women_preferences2 = {
        'W1': ['A', 'C', 'G', 'D', 'F'],
        'W2': ['D', 'F', 'A', 'B'],
        'W3': ['C', 'E', 'F', 'G', 'D'],
        'W4': ['B', 'D', 'A'],
        'W5': ['A', 'F', 'C', 'E']
    }
    result1 = stable_matching_unequal_size(men_preferences1, women_preferences1)
    result2 = stable_matching_incomplete(men_preferences2, women_preferences2)
    print("Stable Matching with unequal size set:", result1)
    print("Stable Matching with incomplete preference lists:", result2)


if __name__ == "__main__":
    main()
