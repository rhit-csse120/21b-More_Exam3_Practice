"""
MORE PRACTICE for Exam 3.

This problem provides practice at: *** MUTATING a list. ***

Authors: David Mutchler, Rachel Krohn, Dave Fisher, Shawn Bohner, Sriram Mohan,
         Amanda Stouder, Vibha Alangar, Mark Hays, Dave Henthorn, Matt Boutell,
         Scott McClellan, Yiji Zhang, Mohammed Noureddine, Steve Chenoweth,
         Claude Anderson, Michael Wollowski, Chandan Rupakheti,
         Derek Whitley, Curt Clifton, Valerie Galluzzi, their colleagues and
         SOLUTION by David Mutchler.
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

import time
import testing_helper


def main():
    """Calls the   TEST   functions in this module."""
    run_test_mutate()


##############################################################################
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


def run_test_mutate():
    """Tests the   mutate   function."""
    print()
    print("--------------------------------------------------")
    print("Testing the   mutate  function:")
    print("--------------------------------------------------")

    format_string = "mutate( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    test_number = 1
    original_argument = [
        [4, 110, 23, 7, 29],
        [],
        [22, 13, 42, 5],
        [21, 21, 28, 6, 28, 15],
    ]
    m = 0
    correct_argument_value_after_function_call = [
        [4, 2, 23, 7, 11],  # 110 and 29 have been replaced with 2 and 11
        [],
        [22, 13, 6, 5],  # 42 has been replaced with 6
        [21, 21, 10, 6, 10, 15],
    ]
    correct_returned_value = None
    run_test(
        mutate,
        original_argument,
        test_number,
        correct_returned_value,
        correct_argument_value_after_function_call,
        test_results,
        format_string,
        [m],
    )

    # Test 2: Same as Test 1 except m=1
    test_number = 2
    original_argument = [
        [4, 110, 23, 7, 29],
        [],
        [22, 13, 42, 5],
        [21, 21, 28, 6, 28, 15],
    ]
    m = 1
    correct_argument_value_after_function_call = [
        [4, 110, 23, 7, 29],
        [],
        [22, 13, 42, 5],
        [21, 21, 28, 6, 28, 15],
    ]
    correct_returned_value = None
    run_test(
        mutate,
        original_argument,
        test_number,
        correct_returned_value,
        correct_argument_value_after_function_call,
        test_results,
        format_string,
        [m],
    )

    # Test 3: Same as Test 1 except m=2
    test_number = 3
    original_argument = [
        [4, 110, 23, 7, 29],
        [],
        [22, 13, 42, 5],
        [21, 21, 28, 6, 28, 15],
    ]
    m = 2
    correct_argument_value_after_function_call = [
        [4, 2, 5, 7, 11],  # 110, 23 and 29 have been replaced with 2, 5 and 11
        [],
        [4, 13, 6, 5],  # 22 and 42 have been replaced with 4 and 6
        [3, 3, 10, 6, 10, 6],
    ]  # 21, 21, 28, 28 and 15 have been replaced
    # with 3, 3, 10, 10 and 6
    correct_returned_value = None
    run_test(
        mutate,
        original_argument,
        test_number,
        correct_returned_value,
        correct_argument_value_after_function_call,
        test_results,
        format_string,
        [m],
    )

    # Test 4: Same as Test 1 except m=3
    test_number = 4
    original_argument = [
        [4, 110, 23, 7, 29],
        [],
        [22, 13, 42, 5],
        [21, 21, 28, 6, 28, 15],
    ]
    m = 3
    correct_argument_value_after_function_call = [
        [4, 110, 23, 7, 29],
        [],
        [22, 13, 42, 5],
        [21, 21, 28, 6, 28, 15],
    ]
    correct_returned_value = None
    run_test(
        mutate,
        original_argument,
        test_number,
        correct_returned_value,
        correct_argument_value_after_function_call,
        test_results,
        format_string,
        [m],
    )

    # Test 5: Same as Test 1 except tuple instead of list
    test_number = 5
    original_argument = (
        [4, 110, 23, 7, 29],
        [],
        [22, 13, 42, 5],
        [21, 21, 28, 6, 28, 15],
    )
    m = 0
    correct_argument_value_after_function_call = (
        [4, 2, 23, 7, 11],  # 110 and 29 have been replaced with 2 and 11
        [],
        [22, 13, 6, 5],  # 42 has been replaced with 6
        [21, 21, 10, 6, 10, 15],
    )
    correct_returned_value = None
    run_test(
        mutate,
        original_argument,
        test_number,
        correct_returned_value,
        correct_argument_value_after_function_call,
        test_results,
        format_string,
        [m],
    )

    # Test 6: A different sequence of sequences
    test_number = 6
    original_argument = (
        [],
        [11, 20, 5, 17, 4, 85, 85, 85],
        [38, 8, 38, 55, 41],
        [38, 8, 7, 55, 6, 7, 17, 3],
        [65, 26],
        [12, 13, 14, 222, 5, 23],
    )
    m = 0
    correct_argument_value_after_function_call = (
        [],
        [11, 20, 5, 17, 4, 85, 85, 85],
        [38, 8, 38, 55, 41],
        [38, 8, 7, 55, 6, 7, 17, 3],
        [65, 26],
        [12, 13, 14, 222, 5, 23],
    )
    correct_returned_value = None
    run_test(
        mutate,
        original_argument,
        test_number,
        correct_returned_value,
        correct_argument_value_after_function_call,
        test_results,
        format_string,
        [m],
    )

    # Test 7: Same as Test 6 except m=1
    test_number = 7
    original_argument = (
        [],
        [11, 20, 5, 17, 4, 85, 85, 85],
        [38, 8, 38, 55, 41],
        [38, 8, 7, 55, 6, 7, 17, 3],
        [65, 26],
        [12, 13, 14, 222, 5, 23],
    )
    m = 1
    correct_argument_value_after_function_call = (
        [],
        [11, 2, 5, 8, 4, 13, 13, 13],
        [11, 8, 11, 10, 5],
        [11, 8, 7, 10, 6, 7, 8, 3],
        [11, 8],
        [3, 4, 5, 6, 5, 5],
    )
    correct_returned_value = None
    run_test(
        mutate,
        original_argument,
        test_number,
        correct_returned_value,
        correct_argument_value_after_function_call,
        test_results,
        format_string,
        [m],
    )

    # Test 8: Same as Test 6 except m=2
    test_number = 8
    original_argument = (
        [],
        [11, 20, 5, 17, 4, 85, 85, 85],
        [38, 8, 38, 55, 41],
        [38, 8, 7, 55, 6, 7, 17, 3],
        [65, 26],
        [12, 13, 14, 222, 5, 23],
    )
    m = 2
    correct_argument_value_after_function_call = (
        [],
        [11, 20, 5, 17, 4, 13, 13, 13],
        [38, 8, 38, 10, 41],
        [38, 8, 7, 10, 6, 7, 17, 3],
        [11, 26],
        [12, 13, 14, 6, 5, 23],
    )
    correct_returned_value = None
    run_test(
        mutate,
        original_argument,
        test_number,
        correct_returned_value,
        correct_argument_value_after_function_call,
        test_results,
        format_string,
        [m],
    )

    # Test 9: Same as Test 6 except m=3
    test_number = 9
    original_argument = (
        [],
        [11, 20, 5, 17, 4, 85, 85, 85],
        [38, 8, 38, 55, 41],
        [38, 8, 7, 55, 6, 7, 17, 3],
        [65, 26],
        [12, 13, 14, 222, 5, 23],
    )
    m = 3
    correct_argument_value_after_function_call = (
        [],
        [2, 2, 5, 8, 4, 13, 13, 13],
        [11, 8, 11, 10, 5],
        [11, 8, 7, 10, 6, 7, 8, 3],
        [11, 8],
        [3, 4, 5, 6, 5, 5],
    )
    correct_returned_value = None
    run_test(
        mutate,
        original_argument,
        test_number,
        correct_returned_value,
        correct_argument_value_after_function_call,
        test_results,
        format_string,
        [m],
    )

    # Test 10: Same as Test 6 except m=4
    test_number = 10
    original_argument = (
        [],
        [11, 20, 5, 17, 4, 85, 85, 85],
        [38, 8, 38, 55, 41],
        [38, 8, 7, 55, 6, 7, 17, 3],
        [65, 26],
        [12, 13, 14, 222, 5, 23],
    )
    m = 4
    correct_argument_value_after_function_call = (
        [],
        [11, 20, 5, 17, 4, 85, 85, 85],
        [38, 8, 38, 55, 41],
        [38, 8, 7, 55, 6, 7, 17, 3],
        [65, 26],
        [12, 13, 14, 222, 5, 23],
    )
    correct_returned_value = None
    run_test(
        mutate,
        original_argument,
        test_number,
        correct_returned_value,
        correct_argument_value_after_function_call,
        test_results,
        format_string,
        [m],
    )

    # Test 11: Same as Test 6 except m=5
    test_number = 11
    original_argument = (
        [],
        [11, 20, 5, 17, 4, 85, 85, 85],
        [38, 8, 38, 55, 41],
        [38, 8, 7, 55, 6, 7, 17, 3],
        [65, 26],
        [12, 13, 14, 222, 5, 23],
    )
    m = 5
    correct_argument_value_after_function_call = (
        [],
        [11, 2, 5, 8, 4, 13, 13, 13],
        [11, 8, 11, 10, 5],
        [11, 8, 7, 10, 6, 7, 8, 3],
        [11, 8],
        [12, 13, 5, 6, 5, 5],
    )
    correct_returned_value = None
    run_test(
        mutate,
        original_argument,
        test_number,
        correct_returned_value,
        correct_argument_value_after_function_call,
        test_results,
        format_string,
        [m],
    )

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


###########################################################################
# IMPORTANT: See the IMPORTANT note in the _TODO_ below.
###########################################################################
def mutate(sequence_of_lists, m):
    """
    What comes in:
      -- A sequence of lists of integers >= 2.
      -- An non-negative integer m less than the number of subsequences.
    What goes out: Nothing (i.e., None).
    Side effects:
       Mutates each of the sub-lists in the sequence of lists so that:
         -- Numbers which are greater than the first (i.e., lowest-index)
              prime in the mth subsequence are replaced with
              their sum_of_digits.
         -- Other numbers are left unchanged.
         -- Note: if there are no primes in the mth subsequence,
              this function does nothing.

       Note that you are given (above) functions for sum_of_digits and is_prime.

    Examples:  In all the examples,
        sequence_of_lists =
                  [[4, 110, 23, 7, 29],
                   [],
                   [22, 13, 42, 5],
                   [21, 21, 28, 6, 28, 15]]
        # Example 1
        m = 0
        problem1(sequence_of_lists, m)
            # The first prime in the 0th subsequence is 23,
            # so after the above, the mutated list
            # (i.e., the list 'sequence_of_lists') is:
            # [[4, 2, 23, 7, 11],  # 110 and 29 have been replaced with 2 and 11
            #  [],
            #  [22, 13, 6, 5],      # 42 has been replaced with 6
            #  [21, 21, 10, 6, 10, 15]]

        # Example 2
        m = 1
        problem1(sequence_of_lists, m)
            # There is no prime in the 1th subsequence,,
            # so after the above, the mutated list
            # (i.e., the list 'sequence_of_lists')
            # is unchanged from what it was.

        # Example 3
        m = 2
        problem1(sequence_of_lists, m)
            # The first prime in the 2th subsequence is 13,
            # so after the above, the mutated list
            # (i.e., the list 'sequence_of_lists') is:
            # [[4, 2, 5, 7, 11],  # 110, 23 and 29 have been replaced with 2, 5 and 11
            #  [],
            #  [4, 13, 6, 5],     # 22 and 42 have been replaced with 4 and 6
            #  [3, 3, 10, 6, 10, 6]]  # 21, 21, 28, 28 and 15 have been replaced
                                      # with 3, 3, 10, 10 and 6
        # Example 4
        m = 3
        problem1(sequence_of_lists, m)
            # There is no prime in the 3th subsequence,,
            # so after the above, the mutated list
            # (i.e., the list 'sequence_of_lists')
            # is unchanged from what it was.

         ** ASK YOUR INSTRUCTOR FOR HELP if these examples  **
      ** and/or the above specification are not clear to you. **

      Type hints:
        :type sequence_of_lists: list[list[int]] | tuple[list[int]]
    """
    ###########################################################################
    # TODO: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #   IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   appropriate   function(s) that are DEFINED ABOVE.
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:     7
    #    TIME ESTIMATE:  15 to 20 minutes.
    # -------------------------------------------------------------------------
    ###########################################################################
    subsequence = sequence_of_lists[m]
    prime = None
    for k in range(len(subsequence)):
        number = subsequence[k]
        if is_prime(number):
            prime = number
            break
    if prime is None:
        return
    for j in range(len(sequence_of_lists)):
        subsequence = sequence_of_lists[j]
        for k in range(len(subsequence)):
            if subsequence[k] > prime:
                sequence_of_lists[j][k] = sum_of_digits(sequence_of_lists[j][k])


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################
def run_test(
    function_to_test,
    argument,
    run_test_number,
    correct_returned_value,
    correct_argument_value_after_function_call,
    test_results,
    format_string,
    additional_arguments,
):
    """
    Runs a test, by calling the given function on the given argument.
    The function should return the given correct_returned_value.
    After the function call, the argument should equal the given
    correct_argument_value_after_function_call.
    Prints messages to indicate whether the test passed or failed.
    """
    print()
    print("Test {}:".format(run_test_number))

    print("  This test case calls:")
    print(format_string.format(*([argument] + additional_arguments)))

    actual_returned_value = function_to_test(argument, *additional_arguments)

    passed_check1 = check_returned_value(actual_returned_value, correct_returned_value)
    passed_check2 = check_argument(argument, correct_argument_value_after_function_call)

    print("  Expected result: ", correct_argument_value_after_function_call)
    print("  Actual result:   ", argument)
    print("  Expected return: ", correct_returned_value)
    print("  Actual return:   ", actual_returned_value)

    if passed_check1 and passed_check2:
        print("  Your code PASSES Test {}.".format(run_test_number), color="blue")
        test_results[0] += 1
    else:
        print("   Your code FAILS Test {}".format(run_test_number), color="red")
        test_results[1] += 1


def check_returned_value(actual_returned_value, correct_returned_value):
    """
    Checks whether the two given returned-values are equal.
    If so, returns True.
    If not, prints an appropriate message and returns False.
    """
    if actual_returned_value == correct_returned_value:
        return True
    else:
        print("  Your code FAILS this test", color="red")
        print("  because it returns the wrong value:", color="red")
        print("    -- The correct returned value is:")
        print("       ", correct_returned_value)
        print("    -- Your code returned this value:")
        print("       ", actual_returned_value)

        return False


def check_argument(actual_argument_value, correct_argument_value):
    """
    Checks whether the two given argument-values are equal.
    If so, returns True.
    If not, prints an appropriate message and returns False.
    """
    if actual_argument_value == correct_argument_value:
        return True
    else:
        print("  Your code FAILS this test because the argument", color="red")
        print("  has the wrong value after the function call:", color="red")
        print("    -- The correct value after the function call is:")
        print("       ", correct_argument_value)
        print("    -- Your actual value after the function call is:")
        print("       ", actual_argument_value)

        return False


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
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print("ERROR - While running this test,", color="red")
    print("your code raised the following exception:", color="red")
    print()
    time.sleep(1)
    raise
