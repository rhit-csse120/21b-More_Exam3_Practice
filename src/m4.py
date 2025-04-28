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
    run_test_number_of_occurrences()


def run_test_number_of_occurrences():
    """Tests the   number_of_occurrences   function."""
    print()
    print("--------------------------------------------------")
    print("Testing the   number_of_occurrences  function:")
    print("--------------------------------------------------")

    format_string = "    number_of_occurrences( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    numbers = [[32, 110, 32, 64, 64], [32, 5, 88], [110, 32, 5], [5]]
    expected = [[4, 2, 4, 2, 2], [4, 3, 1], [2, 4, 3], [3]]

    print_expected_result_of_test([numbers], expected, test_results, format_string)
    actual = number_of_occurrences(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


###########################################################################
# IMPORTANT: See the IMPORTANT note in the _TODO_ below.
###########################################################################
def number_of_occurrences(sequence_of_sequences):
    """
    What comes in:
      -- A sequence of sequences of integers.
    What goes out:
      Returns a list of lists with the same structure as the given
      sequence of sequences, but with each item in the returned list
      of lists being the NUMBER OF OCCURRENCES of the corresponding
      item in the given sequence of sequences.

    Examples:
        # Example 1
        numbers = [[32, 110, 32, 64, 64],
                   [32, 5, 88],
                   [110, 32, 5],
                   [5]]
        number_of_occurrences(numbers) returns:
                  [[4, 2, 4, 2, 2],
                   [4, 3, 1],
                   [2, 4, 3],
                   [3]]
        since there are:
          -- 4 occurrences of 32 in the sequence of sequences
          -- 2 occurrences of 110 in the sequence of sequences
          -- 4 occurrences of 32 in the sequence of sequences
          -- 2 occurrences of 64 in the sequence of sequences
          -- 2 occurrences of 64 in the sequence of sequences
          -- 4 occurrences of 32 in the sequence of sequences
          -- 3 occurrences of 5 in the sequence of sequences
          -- 1 occurrence of 88 in the sequence of sequences
          -- 2 occurrences of 110 in the sequence of sequences
          -- 4 occurrences of 32 in the sequence of sequences
          -- 3 occurrences of 5 in the sequence of sequences
          -- 3 occurrences of 5 in the sequence of sequences

         ** ASK YOUR INSTRUCTOR FOR HELP if these examples  **
      ** and/or the above specification are not clear to you. **

      Type hints:
        :type sequence_of_sequences: list[list[int]] | tuple[list[int]] | tuple[tuple[int]] | list[tuple[int]]
    """
    ###########################################################################
    # TODO: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:     8
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
