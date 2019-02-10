def computeSize(input: float):
    large_cutoff = 60.0
    medium_cutoff = 30.0
    size = "small"
    if input >= large_cutoff:
        size = "large"
    elif input >= medium_cutoff:
        size = "medium"
    return size


if __name__ == '__main__':
    print(computeSize(70.0))
    print(computeSize(50.0))
    print(computeSize(10.0))
