from validation import valid_classes


def test_valid_classes():

    if valid_classes(50, 40):
        print("Test 1 passed")
    else:
        print("Test 1 failed")


def test_invalid_classes():

    if valid_classes(50, 60) == False:
        print("Test 2 passed")
    else:
        print("Test 2 failed")


def test_zero_classes():

    if valid_classes(0, 0) == False:
        print("Test 3 passed")
    else:
        print("Test 3 failed")


test_valid_classes()
test_invalid_classes()
test_zero_classes()