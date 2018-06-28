from math import floor, log2


def get_motor_class(nsec: float):
    """Calculates info about a motor given the total nsec
    Returns a tuple of motor class letter and percent"""
    # motors below 'D' have special
    if nsec < 10:
        if nsec > 5:
            des = 'C'
            percent = 100 * (nsec / 10)
        elif nsec > 2.5:
            des = 'B'
            percent = 100 * (nsec / 5)
        elif nsec > 1.25:
            des = 'A'
            percent = 100 * (nsec / 2.5)
        else:
            des = 'N/A'
            percent = 0

    # all motors above 'D' follow binary powers of 2
    else:

        # Calculate the power of two associated with this ns class
        offset = int(log2(nsec / 10))   # truncate using int()
        des = chr(ord('D') + offset)

        # calculate the percent
        min_ns = 10 * 2 ** offset   # minimum ns in the class range, e.g 'K' has range 1280, 2560
        percent = 100 * (nsec - min_ns) / min_ns

    return des, percent
