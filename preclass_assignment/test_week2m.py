"""Test your functions from Week 2 assignment.
"""
import preclass_assignment.functions as fxn


def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    # when
    fxn.greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Hello, world!\n'  # check that the greeting was what we expect



def test_goldilocks(capsys):
    """Check goldilocks returns expected output"""
     # Test case 1: Bed is too small
    fxn.goldilocks(139)
    captured = capsys.readouterr()
    assert captured.out == "Too small!\n"

    # Test case 2: Bed is just right (140 cm)
    fxn.goldilocks(140)
    captured = capsys.readouterr()
    assert captured.out == "Just right. :)\n"

    # Test case 3: Bed is too large
    fxn.goldilocks(151)
    captured = capsys.readouterr()
    assert captured.out == "Too large!\n"

    # Test case 4: Bed is just right (150 cm)
    fxn.goldilocks(150)
    captured = capsys.readouterr()
    assert captured.out == "Just right. :))\n"


def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    out = fxn.square_list(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match


def test_fibonacci_stop():
    """Check fibonacci functions works as expected."""
    n = 10
    exp_out = [0, 1, 1, 2, 3, 5, 8]
    out = fxn.fibonacci_stop(n)
    assert exp_out == out


def test_clean_pitch():
    """Check clean_pitch works as expected."""
    inp = "good MORNING"
    exp_out = "good morning" 
    out = fxn.clean_pitch(inp)
    assert exp_out == out

