import sys

def main():
    next_biggest_number(sys.argv[1])

def find_left_swap_index(digits):
    left_idx = len(digits) - 2

    # we need to find the first occurance where the number at left_idx is smaller than the number at left_idx + 1
    while left_idx >= 0 and digits[left_idx] >= digits[left_idx + 1]:
        left_idx = left_idx - 1

    return left_idx

def find_right_swap_index(digits, left_swap_idx):
    cursor = left_swap_idx + 1
    smallest_delta = sys.maxsize
    right_swap_idx = cursor

    # We need to find the a digit larger than the digit at the left_swap_idx that has the smallest delta
    # where delta is defined to be the smallest distance been the two digits
    while cursor < len(digits):
        if digits[cursor] > digits[left_swap_idx]:
            delta = digits[cursor] - digits[left_swap_idx]

            if delta < smallest_delta:
                right_swap_idx = cursor
                smallest_delta = delta

        cursor = cursor + 1
            
    return right_swap_idx

def map_digits_to_num(digits):
    string_value = ''.join(map(str, digits))
    return int(string_value)

def next_biggest_number(num):
    digits = [int(x) for x in str(num)]

    left_swap_idx = find_left_swap_index(digits)

    # If the left_swap_idx is less than zero, then the digits are in ascending order and thus no larger number can be made.
    if left_swap_idx < 0:
        return -1
    
    right_swap_idx = find_right_swap_index(digits, left_swap_idx)

    # Swap the digits
    temp = digits[left_swap_idx]
    digits[left_swap_idx] = digits[right_swap_idx]
    digits[right_swap_idx] = temp

    # We only want to sort the digits starting from the left_swap_idx
    digits[left_swap_idx + 1:] = sorted(digits[left_swap_idx + 1:])

    final_num = map_digits_to_num(digits)

    return final_num

if __name__ == "__main__":
    main()



