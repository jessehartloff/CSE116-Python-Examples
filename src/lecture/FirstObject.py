def computeShippingCost(weight):
    if weight < 30:
        return 5.0
    else:
        return 5.0 + (weight - 30.0) * 0.25
