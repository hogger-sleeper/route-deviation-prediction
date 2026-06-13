def levenshtein_distance(planned_route, actual_route):
    """
    Compute Levenshtein (Edit) Distance between two routes.

    Allowed operations:
        1. Insert
        2. Delete
        3. Replace

    Parameters
    ----------
    planned_route : list
    actual_route : list

    Returns
    -------
    int
        Minimum number of edits required.
    """

    m = len(planned_route)
    n = len(actual_route)

    # Create DP table
    dp = []

    for i in range(m + 1):
        row = [0] * (n + 1)
        dp.append(row)

    # Base cases

    # Empty planned -> actual
    for j in range(n + 1):
        dp[0][j] = j

    # Planned -> empty actual
    for i in range(m + 1):
        dp[i][0] = i

    # Fill DP table
    for i in range(1, m + 1):

        for j in range(1, n + 1):

            # Characters (or stops) match
            if planned_route[i - 1] == actual_route[j - 1]:

                dp[i][j] = dp[i - 1][j - 1]

            else:

                insert_cost = dp[i][j - 1]
                delete_cost = dp[i - 1][j]
                replace_cost = dp[i - 1][j - 1]

                dp[i][j] = 1 + min(
                    insert_cost,
                    delete_cost,
                    replace_cost
                )

    return dp[m][n]



def calculate_eds(planned_route, actual_route):

    # Calculate Levenshtein Edit Distance
    edit_distance = levenshtein_distance(
        planned_route,
        actual_route
    )

    # According to the paper:
    # EDS = Edit Distance / Length of Planned Route

    if len(planned_route) == 0:
        return 0.0

    eds = edit_distance / len(planned_route)

    return round(eds, 4)
# -------------------------
# Test Cases
# -------------------------

if __name__ == "__main__":

    planned = ["A", "B", "C"]
    actual = ["A", "C"]

    print("EDS Score :", calculate_eds(
        planned,
        actual
    ))

    print()

    planned2 = ["C", "A", "T"]
    actual2 = ["C", "U", "T"]

    print("EDS Score :", calculate_eds(
        planned2,
        actual2
    ))
