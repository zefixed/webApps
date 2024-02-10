import subprocess
import pytest
# from arithmetic_operators import arithmetic_operators
# from division import division
# from loops import loops
# from print_function import print_function
# from second_score import second_score
# from nested_list import nested_list
# from lists import lists
# from swap_case import swap_case
# from split_and_join import split_and_join
# from max_word import max_word
# from price_sum import price_sum
# from anagram import anagram
# from metro import metro
# from is_leap import is_leap
# from happiness import happiness
# from matrix_mult import matrix_mult

INTERPRETER = 'python'

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    "python_if_else": [
        ("1", "Weird"),
        ("4", "Not Weird"),
        ("3", "Weird"),
        ("6","Weird"),
        ("22", "Not Weird")
    ],
    "arithmetic_operators": [
        ("1\n2", "3\n-1\n2"),
        ("10\n5", "15\n5\n50"),
        ("4\n7", "11\n-3\n28"),
        ("23465789\n98237465", "121703254\n-74771676\n2305219625584885"),
    ],
    "division": [
        ("1\n2", "0\n0.5"),
        ("10\n2", "5\n5.0"),
        ("15\n4", "3\n3.75"),
        ("20\n7", "2\n2.857142857142857"),
    ],
    "loops": [
        ("1", "0"),
        ("2", "0\n1"),
        ("3", "0\n1\n4"),
        ("4", "0\n1\n4\n9"),
    ],
    "print_function": [
        ("1", "1"),
        ("2", "12"),
        ("3", "123"),
        ("4", "1234"),
    ],
    "second_score": [
        ("5\n2 3 6 6 5", "5"),
        ("6\n12 45 23 78 38 34", "45"),
        ("7\n123 789 978 345 785 425 987", "978"),
        ("8\n9746 6354 9785 7643 6352 3657 8978 9764", "9764"),
    ],
    "nested_list": [
        ("5\nHarry\n37.21\nBerry\n37.21\nTina\n37.2\nAkriti\n41\nHarsh\n39", "Berry\nHarry"),
        ("5\nAlice\n90.5\nBob\n85.0\nCharlie\n92.0\nDavid\n85.0\nEve\n88.5\n", "Eve"),
        ("3\nAlice\n90.5\nBob\n85.0\nCharlie\n92.0\n", "Alice"),
        ("4\nAlice\n81.0\nBob\n85.0\nCharlie\n85.0\nDavid\n85.0\n", "Bob\nCharlie\nDavid"),
    ],
    "lists": [
        ("4\nappend 1\nappend 2\ninsert 1 3\nprint", "[1, 3, 2]"),
        ("12\ninsert 0 5\ninsert 1 10\ninsert 0 6\nprint\nremove 6\nappend 9\nappend 1\nsort\nprint\npop\nreverse\nprint", "[6, 5, 10]\n[1, 5, 9, 10]\n[9, 5, 1]"),
        ("3\nappend 1\nappend 2\nprint", "[1, 2]"),
        ("0\n", ""),
    ],
    "swap_case": [
        ("", ""),
        ("Www.MosPolytech.ru", "wWW.mOSpOLYTECH.RU"),
        ("Pythonist 2", "pYTHONIST 2"),
        ("iouGuoyfUTYf7ituDtyfcTYU", "IOUgUOYFutyF7ITUdTYFCtyu"),
    ],
    "split_and_join": [
        ("this is a string", "this-is-a-string"),
        ("To be or not to be", "To-be-or-not-to-be"),
        ("This is not a string, this is object", "This-is-not-a-string,-this-is-object"),
        ("P y t h o n", "P-y-t-h-o-n"),
    ],
    "anagram": [
        ("qweasdzxc\nasdcxzqwe", "YES"),
        ("false\nleafs", "YES"),
        ("jsjsfgjwrjt\njsjcvbjwrjt", "NO"),
        ("oqenrbopqernb\nasdnrbopqbnmb", "NO"),
    ],
    "metro": [
        ("5\n12 34\n23 87\n32 98\n45 67\n78 90\n65", "3"),
        ("5\n12 38\n38 38\n32 98\n45 67\n78 90\n38", "3"),
        ("5\n12 24\n12 12\n32 98\n45 67\n78 90\n12", "2"),
        ("5\n56 56\n56 56\n56 56\n56 56\n56 56\n56", "5"),
    ],
    "is_leap": [
        ("1900", "False"),
        ("2000", "True"),
        ("2004", "True"),
        ("100000", "True"),
    ],
    "happiness": [
        ("3 2\n1 5 3\n3 1\n5 7", "1"),
        ("10 5\n1 5 3 5 3 6 8 0 5 1\n0 1 2 3 4\n5 6 7 8 9", "0"),
        ("10 5\n0 0 0 0 0 0 0 0 0 0\n0 1\n9", "10"),
        ("10 5\n0 0 0 0 0 0 0 0 0 0\n9\n0 1", "-10"),
    ],
    "matrix_mult": [
        ("3\n1 2 3\n4 5 6\n7 8 9\n9 8 7\n6 5 4\n3 2 1", "30 24 18\n84 69 54\n138 114 90"),
        ("3\n1 0 0\n0 1 0\n0 0 1\n9 8 7\n6 5 4\n3 2 1", "9 8 7\n6 5 4\n3 2 1"),
        ("3\n0 0 0\n0 0 0\n0 0 0\n9 8 7\n6 5 4\n3 2 1", "0 0 0\n0 0 0\n0 0 0"),
        ("3\n-1 -2 -3\n-4 -5 -6\n-7 -8 -9\n9 8 7\n6 5 4\n3 2 1", "-30 -24 -18\n-84 -69 -54\n-138 -114 -90"),
    ],
    "minion_game": [
        ("BANANA", "Стюарт 12"),
        ("ALABAMA", "Кевин 16"),
        ("OBAMA", "Кевин 9"),
        ("MAMBA", "Стюарт 10"),
    ],
    "pirate_ship": [
        ("30 5\nЗолото 30 100\nСеребро 20 60\nБриллианты 5 300\nРом 20 40\nМонеты 10 80", "Бриллианты 5 300\nМонеты 10 80\nЗолото 15 50.0"),
    ],
    
    
}
def test_hello_world():
    assert run_script('hello.py') == 'Hello, world!'

@pytest.mark.parametrize("input_data, expected", test_data['python_if_else']) # 4 tests
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators']) # 4 tests
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', [input_data]) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data["division"]) # 4 tests
def test_division(input_data, expected):
    assert run_script('division.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data["loops"]) # 4 tests
def test_loops(input_data, expected):
    assert run_script('loops.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data["print_function"]) # 4 tests
def test_print_function(input_data, expected):
    assert run_script('print_function.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data["second_score"]) # 4 tests
def test_second_score(input_data, expected):
    assert run_script('second_score.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data["nested_list"]) # 4 tests
def test_nested_list(input_data, expected):
    assert run_script('nested_list.py', [input_data]) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data["lists"]) # 4 tests
def test_lists(input_data, expected):
    assert run_script('lists.py', [input_data]) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data["swap_case"]) # 4 tests
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', [input_data]) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data["split_and_join"]) # 4 tests
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', [input_data]) == expected
    
def test_max_word(): # 1 test
    assert run_script('max_word.py') == 'сосредоточенности'

def test_price_sum(): # 1 test
    assert run_script('price_sum.py') == '6842.84 5891.06 6810.9'
    
@pytest.mark.parametrize("input_data, expected", test_data["anagram"]) # 4 tests
def test_anagram(input_data, expected):
    assert run_script('anagram.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data["metro"]) # 4 tests
def test_metro(input_data, expected):
    assert run_script('metro.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data["is_leap"]) # 4 tests
def test_is_leap(input_data, expected):
    assert run_script('is_leap.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data["happiness"]) # 4 tests
def test_happiness(input_data, expected):
    assert run_script('happiness.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data["matrix_mult"]) # 4 tests
def test_matrix_mult(input_data, expected):
    assert run_script('matrix_mult.py', [input_data]) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data["minion_game"]) # 4 tests
def test_minion_game(input_data, expected):
    assert run_script('minion_game.py', [input_data]) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data["pirate_ship"]) # 4 tests
def test_pirate_ship(input_data, expected):
    assert run_script('pirate_ship.py', [input_data]) == expected
