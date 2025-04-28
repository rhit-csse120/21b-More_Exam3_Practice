"""
MORE PRACTICE for Exam 3.

This problem provides practice at:
  *** ITERATING (looping) through a SEQUENCE OF SEQUENCES. ***

Authors: David Mutchler, Rachel Krohn, Dave Fisher, Shawn Bohner, Sriram Mohan,
         Amanda Stouder, Vibha Alangar, Mark Hays, Dave Henthorn, Matt Boutell,
         Scott McClellan, Yiji Zhang, Mohammed Noureddine, Steve Chenoweth,
         Claude Anderson, Michael Wollowski, Chandan Rupakheti,
         Derek Whitley, Curt Clifton, Valerie Galluzzi, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

"""
Academic Integrity: I got help on this module from:
         PUT_HERE_THE_NAMES_OF_PEOPLE_WHO_HELPED_YOU_ON_THIS_MODULE_(IF_ANY).
"""  # TODO: If you got help from anyone on this module, list their names here.

###############################################################################
# TODO: 2.
#  Students:
#  __
#  These problems have DIFFICULTY and TIME ratings:
#    DIFFICULTY rating:  1 to 10, where:
#       1 is very easy
#       3 is an "easy" Exam 3 question.
#       5 is a "typical" Exam 3 question.
#       7 is a "hard" Exam 3 question.
#      10 is an EXTREMELY hard problem (too hard for a Exam 3 question)
#  __
#    TIME ratings: A ROUGH estimate of the number of minutes that we
#       would expect a well-prepared student to take on the problem.
#  __
#    IMPORTANT: For ALL the problems in this module,
#      if you reach the time estimate and are NOT close to a solution,
#      STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP on it,
#      in class or via Piazza.
#  __
#  After you read (and understand) the above, change this _TODO_ to DONE.
###############################################################################

import random
import time
import testing_helper


def main():
    """Calls the   TEST   functions in this module."""
    run_test_practice1()


###############################################################################
# TODO: 3.  READ the green doc-strings for the:
#     - is_prime
#     - sum_of_digits
#   functions defined below.  They are the same as you have seen previously.
#   You do NOT need to understand their implementations,
#   just their specification (per their doc-strings).
#  _
#   You should  ** CALL **  those functions as needed in implementing the
#   other functions.  After you have READ this, change its _TODO_ to DONE.
###############################################################################


def is_prime(n):
    """
    What comes in:  An integer n >= 2.
    What goes out:
      -- Returns True if the given integer is prime,
         else returns False.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
    Note: The algorithm used here is simple and clear but slow.
    """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True


def sum_of_digits(number):
    """
    What comes in:  An integer.
    What goes out:  Returns the sum of the digits in the given integer.
    Side effects:   None.
    Example:
      If the integer is 83135,
      this function returns (8 + 3 + 1 + 3 + 5), which is 20.
    """
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit_sum = digit_sum + (number % 10)
        number = number // 10

    return digit_sum
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_prime  or  sum_of_digits  functions;
    #   they have no _TODO_.  Do NOT copy code from these functions.
    # Instead, ** CALL ** these function as needed in the problems below.
    # -------------------------------------------------------------------------


def run_test_practice1():
    """Tests the   practice1   function."""
    print()
    print("--------------------------------------------------")
    print("Testing the   practice1  function:")
    print("--------------------------------------------------")

    format_string = "    practice1( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    numbers = [
        [32, 110, 72, 64, 61],  # sum_of_digits: 5, 2, 9, 10, 7
        [],
        [110, 91, 42],
    ]  # sum_of_digits: 2, 10, 6
    expected = [32, 110, 61, 110]  # Items associated with prime sum_of_digits
    print_expected_result_of_test([numbers], expected, test_results, format_string)
    actual = practice1(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    numbers = [
        [825, 11, 140],  # sum_of_digits: 15, 2, 5
        [32, 110, 72, 64, 61],  # sum_of_digits: 5, 2, 9, 10, 7
        [],
        [111, 91, 59, 4441],
    ]  # sum_of_digits: 3, 10, 14, 13
    expected = [11, 140, 32, 110, 61, 111, 4441]  # For primes 5, 2, 7, 3 and 13
    print_expected_result_of_test([numbers], expected, test_results, format_string)
    actual = practice1(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    numbers = [
        [100000],  # sum_of_digits: 1, and 1 is treated as prime
        [0],
    ]  # sum_of_digits: 0, and 0 is treated as prime
    expected = [100000, 0]  # Items associated with primes 1 and 0, respectively
    print_expected_result_of_test([numbers], expected, test_results, format_string)
    actual = practice1(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:  Same as Test 3, but tuples
    numbers = (
        (100000,),  # sum_of_digits: 1, and 1 is treated as prime
        (0,),
    )  # sum_of_digits: 0, and 0 is treated as prime
    expected = [100000, 0]  # Items associated with primes 1 and 0, respectively
    print_expected_result_of_test([numbers], expected, test_results, format_string)
    actual = practice1(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    numbers = [(2, 3, 5, 7), (11, 16, 92, 29, 913), [29, 9992, 2999, 9299, 9929, 9992]]
    expected = [2, 3, 5, 7, 11, 16, 92, 29, 913, 29, 9992, 2999, 9299, 9929, 9992]
    print_expected_result_of_test([numbers], expected, test_results, format_string)
    actual = practice1(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    numbers = [(22, 213, 35, 27), (211, 13, 17, 19, 123), [219, 31, 37]]
    expected = []
    print_expected_result_of_test([numbers], expected, test_results, format_string)
    actual = practice1(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    numbers = [(2, 3), (11, 13, 17, 19, 23, 100, 1000), [29, 31]]
    expected = [2, 3, 11, 23, 100, 1000, 29]
    print_expected_result_of_test([numbers], expected, test_results, format_string)
    actual = practice1(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8 and following:
    random.seed(42)  # Ensures repeatability
    numbers = [[11111, 4, 6, 19], [], [60, 62, 63, 1111, 1, 1111, 4, 6666, 66, 6], []]
    for k in range(100):
        random.shuffle(numbers[0])
        random.shuffle(numbers[2])
        expected = [11111, 1]
        print_expected_result_of_test([numbers], expected, test_results, format_string)
        actual = practice1(numbers)
        print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


###########################################################################
# IMPORTANT: See the IMPORTANT note in the _TODO_ below.
###########################################################################
def practice1(sequence_of_sequences):
    """
    What comes in:
      -- A sequence of sequences of non-negative integers.
    What goes out:
      Returns a list of all the numbers in the given
      sequence of sequences whose sum of digits is prime.
      (Maintains the same order as in the given sequence of sequences.)

      Note that you are given (above) functions for sum_of_digits and is_prime.

    Examples:
        # Example 1
        numbers = [[32, 110, 72, 64, 61],   # sum_of_digits: 5, 2, 9, 10, 7
                   [],
                   [110, 91, 42]]           # sum_of_digits: 2, 10, 6

        result = practice1(numbers)  # result will be [32, 110, 61, 110]
                                    # because those are the items whose
                                    # sum_of_digits are 5, 2, 7 and 2,
                                    # respectively, all of which are prime.

        # Example 2
        numbers = [[825, 11, 140],          # sum_of_digits: 15, 2, 5
                   [32, 110, 72, 64, 61],   # sum_of_digits: 5, 2, 9, 10, 7
                   [],
                   [111, 91, 59, 4441]]     # sum_of_digits: 3, 10, 14, 13
        result = practice1(numbers)
                         # result will be [11, 140, 32, 110, 61, 111, 4441]
                         # because those are the items whose sum_of_digits
                         # are 2, 5, 5, 2, 7, 3 and 13, respectively,
                         # all of which are prime.

        # Example 3
        numbers = [[100000],     # sum_of_digits: 1, and 1 is treated as prime
                   [0]]          # sum_of_digits: 0, and 0 is treated as prime
        result = practice1(numbers)     # result will be [100000, 0]

         ** ASK YOUR INSTRUCTOR FOR HELP if these examples  **
      ** and/or the above specification are not clear to you. **

      Type hints:
        :type sequence_of_sequences: list[list[int]] | tuple[list[int]] | tuple[tuple[int]] | list[tuple[int]]
    """
    ###########################################################################
    # TODO: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #   IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   appropriate   function(s) that are DEFINED ABOVE.
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:     5
    #    TIME ESTIMATE:  10 minutes.
    # -------------------------------------------------------------------------
    ###########################################################################


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################
def print_expected_result_of_test(
    arguments, expected, test_results, format_string, suffix=""
):
    testing_helper.print_expected_result_of_test(
        arguments, expected, test_results, format_string, suffix
    )


def print_actual_result_of_test(expected, actual, test_results, precision=None):
    testing_helper.print_actual_result_of_test(
        expected, actual, test_results, precision
    )


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The  IF  statement helps prevent   main   from running
# when we are doing special testing within a testing framework.
# The   try .. except   helps prevent error messages on the console
# from being intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("ERROR - While running this test,", color="red")
        print("your code raised the following exception:", color="red")
        print()
        time.sleep(1)
        raise
