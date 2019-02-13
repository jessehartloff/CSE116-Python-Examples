# Returns the number of consecutive 0's at the end of a list
def check_end_of_list(input_list: list) -> int:
    input_list.reverse()
    count = 0
    for i in input_list:
        if i == 0:
            count += 1
        else:
            break
    return count


if __name__ == '__main__':
    numbers = [5, 8, 2, 9, 0, 0, 0]

    zeros = check_end_of_list(numbers)
    print(zeros)  # correctly prints 3

    zeros_again = check_end_of_list(numbers)
    print(zeros_again)  # prints 0

    # The list was passed by reference (memory address) and was reversed during the first call
    # The second call received a reversed list!

    # *Common mistake with lists of sounds in Rhyming Dictionary
