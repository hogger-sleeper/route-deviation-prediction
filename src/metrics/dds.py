def calculate_dds(planned_distance,
                  actual_distance):
    """
    Calculate Distance Deviation Score.

    DDS = (Actual - Planned) / Planned

    Parameters
    ----------
    planned_distance : float
    actual_distance : float

    Returns
    -------
    float
    """

    if planned_distance == 0:
        return 0.0

    dds = (
        actual_distance -
        planned_distance
    ) / planned_distance

    return round(dds, 4)


# -------------------------
# Test
# -------------------------

if __name__ == "__main__":

    planned = 100.0
    actual = 115.0

    score = calculate_dds(
        planned,
        actual
    )

    print("Planned Distance :", planned)
    print("Actual Distance  :", actual)
    print("DDS Score        :", score)