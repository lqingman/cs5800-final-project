"""
Final project code
Qingman Li
weakly stable matching with ties in preference lists
"""


def convert_preferences_to_ranking(women_preferences):
    """
    A helper function to convert the preferences list to a ranking dictionary
    """
    woman_ranking = {}

    for woman, preferences in women_preferences.items():
        ranking = {}
        for rank, preference_list in enumerate(preferences):
            for man in preference_list:
                ranking[man] = rank
        woman_ranking[woman] = ranking

    return woman_ranking


def stable_matching_with_ties_weak(men_preferences, women_preferences):

    # Generate a ranking for each woman with ties considered
    women_rankings = convert_preferences_to_ranking(women_preferences)
    # Initialize all men to be free
    free_men = list(men_preferences.keys())
    engaged_pairs = {}

    # While there is a free man who hasn't proposed to every woman
    while free_men:
        # Select the first free man (m)
        m = free_men[0]
        # Skip any empty preference lists
        while men_preferences[m] and not men_preferences[m][0]:
            men_preferences[m].pop(0)

        # If there are no more preferences left for m, remove him from free_men and continue
        if not men_preferences[m]:
            free_men.remove(m)
            continue

        # Get the first group of women on m's list (w_list)
        w_list = men_preferences[m][0]

        for w in w_list:
            if w in engaged_pairs:
                x = engaged_pairs[w]
                free_men.append(x)

            # Engage m to w
            engaged_pairs[w] = m
            free_men.remove(m)

            # Get the rank of m in w's list
            rank_of_m = women_rankings[w][m]

            # Remove all men ranked the same or worse than m from w's list
            successors = []
            for man, rank in women_rankings[w].items():
                if rank >= rank_of_m:
                    successors.append(man)

            for successor in successors:
                for pref_group in men_preferences[successor]:
                    if w in pref_group:
                        pref_group.remove(w)
                        break  # Since w will appear only once in each man's preferences

            # Truncate w's preference list to remove all men from rank_of_m onwards
            women_preferences[w] = [
                group for rank, group in enumerate(women_preferences[w]) if rank < rank_of_m
            ]
            # Append back m to the end of w's preference list
            women_preferences[w].append([m])

            # Break the loop since m is now engaged
            break

    return engaged_pairs


def main():
    """
    main program
    """
    # Example usage with ties
    men_preferences = {
        "A": [["X", "Y"], ["Z"], ["W"]],
        "B": [["Z"], ["W"], ["X", "Y"]],
        "C": [["Y", "W"], ["Z"], ["X"]],
        "D": [["W"], ["X"], ["Y"], ["Z"]]
    }

    women_preferences = {
        "X": [["C"], ["B", "A"], ["D"]],
        "Y": [["A"], ["D"], ["C", "B"]],
        "Z": [["A", "D"], ["B"], ["C"]],
        "W": [["B"], ["C"], ["D"], ["A"]]
    }

    men_preferences2 = {
        "M1": [["W3", "W2"], ["W1"], ["W4"]],
        "M2": [["W2"], ["W4"], ["W1", "W3"]],
        "M3": [["W2", "W4"], ["W3"], ["W1"]],
        "M4": [["W4"], ["W1", "W2"], ["W3"]]
    }

    women_preferences2 = {
        "W1": [["M3"], ["M2", "M1"], ["M4"]],
        "W2": [["M4"], ["M1"], ["M3", "M2"]],
        "W3": [["M2", "M4"], ["M1"], ["M3"]],
        "W4": [["M2", "M3"], ["M4"], ["M1"]]
    }

    result = stable_matching_with_ties_weak(men_preferences, women_preferences)
    print("Engaged pairs:", result)
    result2 = stable_matching_with_ties_weak(men_preferences2, women_preferences2)
    print("Engaged pairs:", result2)


if __name__ == "__main__":
    main()
