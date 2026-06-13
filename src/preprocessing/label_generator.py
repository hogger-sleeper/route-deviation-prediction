def generate_label(rqs, eds, dds):
    """
    Generate route label.

    ND = Non-Deviated
    D  = Deviated
    """

    if (
        rqs >= 0.85 and
        eds <= 0.30 and
        abs(dds) <= 0.03
    ):
        return "ND"

    return "D"


# ----------------------
# Test
# ----------------------

if __name__ == "__main__":

    print(
        generate_label(
            1.0,
            0.0,
            0.0
        )
    )

    print(
        generate_label(
            0.50,
            0.60,
            0.10
        )
    )