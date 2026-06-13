from collections import defaultdict


def calculate_rqs(planned_route, actual_route):

    if len(planned_route) != len(actual_route):
        raise ValueError(
            "Planned and Actual routes must have equal length."
        )

    n = len(planned_route)

    if n <= 1:
        return 1.0

    # --------------------------
    # Build occurrence maps
    # --------------------------

    planned_positions = defaultdict(list)
    actual_positions = defaultdict(list)

    for idx, stop in enumerate(planned_route):
        planned_positions[stop].append(idx)

    for idx, stop in enumerate(actual_route):
        actual_positions[stop].append(idx)

    # --------------------------
    # Numerator
    # --------------------------

    total_shift = 0

    for stop in planned_positions:

        for p, a in zip(
            planned_positions[stop],
            actual_positions[stop]
        ):

            total_shift += abs(a - p)

    # --------------------------
    # Denominator
    # --------------------------

    max_shift = 0

    for i in range(1, n + 1):
        max_shift += abs((2 * i) - (n + 1))

    # --------------------------
    # Final RQS
    # --------------------------

    rqs = 1 - (total_shift / max_shift)

    return round(rqs, 4)

if __name__ == "__main__":

    planned = [0, 1, 2, 3, 3, 0, 1]
    actual = [0, 3, 3, 0, 1, 2, 1]

    score = calculate_rqs(
        planned,
        actual
    )

    print("Planned Route :", planned)
    print("Actual Route  :", actual)
    print("RQS Score     :", score)