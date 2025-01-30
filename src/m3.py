"""
MORE PRACTICE for Exam 3.

This problem provides practice at:
   *** using MULTIPLE VARIABLES in a loop to maintain STATE data. ***

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

import time
import testing_helper
import random


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_get_second_largest()


def run_test_get_second_largest():
    """ Tests the   get_second_largest   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   get_second_largest   function:")
    print("--------------------------------------------------")

    format_string = "  get_second_largest(\n   {},\n   {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 100
    sequence = [940, 390, 83, 5, 403, 100, 40]
    m = 4
    print_expected_result_of_test([m, sequence], expected, test_results,
                                  format_string)
    actual = get_second_largest(m, sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 40
    sequence = [940, 390, 83, 5, 403, 100, 40]
    m = 2
    print_expected_result_of_test([m, sequence], expected, test_results,
                                  format_string)
    actual = get_second_largest(m, sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 390
    sequence = [940, 390, 83, 5, 403, 100, 40]
    m = 6
    print_expected_result_of_test([m, sequence], expected, test_results,
                                  format_string)
    actual = get_second_largest(m, sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 100
    sequence = [940, 390, 83, 5, 403, 100, 40]
    m = 3
    print_expected_result_of_test([m, sequence], expected, test_results,
                                  format_string)
    actual = get_second_largest(m, sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 100
    sequence = [940, 390, 83, 5, 403, 100, 40]
    m = 5
    print_expected_result_of_test([m, sequence], expected, test_results,
                                  format_string)
    actual = get_second_largest(m, sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 403
    sequence = [940, 390, 83, 5, 403, 100, 40]
    m = 7
    print_expected_result_of_test([m, sequence], expected, test_results,
                                  format_string)
    actual = get_second_largest(m, sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Tests 7 and following:
    random.seed(42)  # Make the tests able to be replicated.
    expected = 42
    sequence = [10, 20, 21, 25, 30, 40, 41, 42, 100]
    m = 9
    for k in range(1000):
        test_sequence = sequence.copy()
        random.shuffle(test_sequence)
        print_expected_result_of_test([m, test_sequence], expected,
                                      test_results, format_string)
        actual = get_second_largest(m, test_sequence)
        print_actual_result_of_test(expected, actual, test_results)
    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


################################################################################
# See the IMPORTANT HINT below for one way to solve the following problem.
################################################################################
def get_second_largest(m, sequence):
    """
    What comes in:
      -- An integer m that is at least 2, and
      -- a list of integers whose length is at least 2 and at most m.
    What goes out:
      -- Returns the second-largest number in the last m items in the sequence.
    Side effects:   None.
    Examples:
      get_second_largest( 4, [940, 490, 83, 5, 403, 100, 40] ) returns 100
         (because m=4 means the last 4 items, which are 5, 403, 100 and 40,
          and 100 is the second-largest of those four numbers.
      get_second_largest( 2, [940, 390, 83, 5, 403, 100, 40] ) returns 40
         (because m=2 means the last 2 items, which are 100 and 40,
          and 40 is the second-largest of those two numbers.
      get_second_largest( 6, [940, 390, 83, 5, 403, 100, 40] ) returns 390
         (because m=6 means the last 6 items,
          which are 390, 83, 5, 403, 100 and 40,
          and 390 is the second-largest of those six numbers.

      get_second_largest( 3, [940, 390, 83, 5, 403, 100, 40] ) returns 100
      get_second_largest( 5, [940, 390, 83, 5, 403, 100, 40] ) returns 100
      get_second_largest( 7, [940, 390, 83, 5, 403, 100, 40] ) returns 403

                ** ASK YOUR INSTRUCTOR FOR HELP **
        ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **

    Type hints:
      :type m: int
      :type sequence: list[int] | tuple[int]
    """
    ###########################################################################
    # TODO: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #   IMPORTANT HINT: There are many ways to solve this problem.
    #   One way is to keep track of the largest and second-largest items,
    #   and adjust each of these as needed as you process the list.
    #   Note that this is NOT a NESTED sequence problem!
    #   _
    #   You get full credit for any correct way of solving this problem.
    #   Ways that MUTATE the list will get most, but not all, of the credit.
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:     10
    #    TIME ESTIMATE:  20 minutes.
    # -------------------------------------------------------------------------
    ###########################################################################


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################
def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string, suffix=""):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix)


def print_actual_result_of_test(expected, actual, test_results,
                                precision=None):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results, precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Use False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try ... except   prevents error messages on the console from being
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
