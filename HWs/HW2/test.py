import subprocess
import pytest

INTERPRETER = "python"

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input="\n".join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    "fact": [
        (5, 120),
        (10, 3628800),
        (0, 1),
        (-1, 0),
        (100, 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000),
    ],
    "show_employee": [
        (["Иванов Иван Иванович", 30000], "Иванов Иван Иванович: 30000 ₽"),
        (["Иванов Иван Иванович", 9832450978634508796], "Иванов Иван Иванович: 9832450978634508796 ₽"),
        (["Иванов Иван Иванович", 0], "Иванов Иван Иванович: 0 ₽"),
        (["Иванов Иван Иванович"], "Иванов Иван Иванович: 100000 ₽"),
        (["Иванов Иван Иванович", -100000], "Иванов Иван Иванович: -100000 ₽"),
    ],
    "sum_and_sub": [
        ([0, 0], [0, 0]),
        ([1, 1], [2, 0]),
        ([0, -1], [-1, 1]),
        ([-1, -1], [-2, 0]),
        ([86795345, 897345], [87692690, 85898000]),
        ([65789045938074378960, 9873249057843608975432], [9939038103781683354392, -9807460011905534596472]),
    ],
    "process_list": [
        ([1, 2], [1, 4]),
        ([0], [0]),
        ([], []),
        ([-2, -1, 0, 1, 2], [4, -1, 0, 1, 4]),
    ],
    "my_sum": [
        ([], 0.0),
        ([0], 0.0),
        ([0, 1, 2], 3.0),
        ([-2, -1, 0, 1, 2], 0.0),
        ([123, 456, 789], 1368.0),
        ([987, 654, 321], 1962.0),
        ([1.1, 2.2, 3.3], 6.6),
    ],
    "my_sum_argv": [
        ("python my_sum_argv.py 1 2 3 4 5", "15.0"),
        ("python my_sum_argv.py", "0.0"),
        ("python my_sum_argv.py 0", "0.0"),
        ("python my_sum_argv.py -2 -1 0 1 2", "0.0"),
        ("python my_sum_argv.py 123 456 789", "1368.0"),
        ("python my_sum_argv.py 987 654 321", "1962.0"),
        ("python my_sum_argv.py 1.1 2.2 3.3", "6.6"),
    ],
    "files_sort": [
        ("python ./files_sort.py ./test_dir", "a.py\nb.py\nc.py\na.txt\naa.txt\nb.txt\nc.txt"),
    ],
    "file_search": [
        ("python file_search.py a.txt", "1\n2\n3\n4\n5"),
        ("python file_search.py b.txt", ""),
        ("python file_search.py qwe.txt", "Файл qwe.txt не найден"),
    ],
    "email_validation": [
        ("3\nlara@mospolytech.ru\nbrian-23@mospolytech.ru\nbritts_54@mospolytech.ru", "['brian-23@mospolytech.ru', 'britts_54@mospolytech.ru', 'lara@mospolytech.ru']"),
        ("1\nl@l.l", "['l@l.l']"),
        ("0", "[]"),
        ("", ""),
        ("1\n.@re.re", "[]"),
        ("1\n_@re.re", "['_@re.re']"),
        ("1\n%@re.re", "[]"),
        ("1\nqwe@.re", "[]"),
    ],
    "fibonacci": [
        ("-1", "[]"),
        ("0", "[]"),
        ("1", "[0]"),
        ("2", "[0, 1]"),
        ("5", "[0, 1, 1, 8, 27]"),
        ("10", "[0, 1, 1, 8, 27, 125, 512, 2197, 9261, 39304]"),
    ],
    "compute_average_scores": [
        ("5 3\n89 90 78 93 80\n90 91 85 88 86\n91 92 83 89 90.5", "90.0\n91.0\n82.0\n90.0\n85.5"),
        ("3 3\n89 90 78\n90 91 85\n91 92 83", "90.0\n91.0\n82.0"),
        ("3 3\n0 0 0\n0 0 0\n0 0 0", "0.0\n0.0\n0.0"),
        ("3 3\n100 100 100\n100 100 100\n100 100 100", "100.0\n100.0\n100.0"),
    ],
    "phone_number": [
        ("3\n07895462130\n89875641230\n9195969878", "+7 (789) 546-21-30\n+7 (987) 564-12-30\n+7 (919) 596-98-78"),
    ],
    "phone_number": [
        ("5\nAndr Bus 30 M\nMike Thomson 20 M\nRobert Bustle 32 M\nAndria Bustle 30 F\nAndr Bus 30 M", ""),
    ],
}

from fact import fact_rec, fact_it
from show_employee import show_employee
from sum_and_sub import sum_and_sub
from process_list import process_list, process_list_gen
from my_sum import my_sum
from my_sum_argv import my_sum_argv
from files_sort import files_sort
from file_search import file_search
from email_validation import filter_mail
from average_scores import compute_average_scores

@pytest.mark.parametrize("input_data, expected", test_data["fact"])
def test_fact_it(input_data, expected):
    assert fact_it(input_data) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data["fact"])
def test_fact_rec(input_data, expected):
    assert fact_rec(input_data) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data["show_employee"])
def test_show_employee(input_data, expected):
    if len(input_data) == 2:
        assert show_employee(input_data[0], input_data[1]) == expected
    else:
        assert show_employee(input_data[0]) == expected

@pytest.mark.parametrize("input_data, expected", test_data["sum_and_sub"])
def test_sum_and_sub(input_data, expected):
    assert sum_and_sub(input_data[0], input_data[1]) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data["process_list"])
def test_process_list(input_data, expected):
    assert process_list(input_data) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data["process_list"])
def test_process_list_gen(input_data, expected):
    assert process_list_gen(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data["my_sum"])
def test_my_sum(input_data, expected):
    assert my_sum(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['my_sum_argv'])
def test_my_sum_argv(input_data, expected):
    input_data = input_data.split(" ")
    command, filename, *args  = input_data
    assert subprocess.check_output([command, filename, *args], encoding="cp1251").strip() == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['files_sort'])
def test_files_sort(input_data, expected):
    input_data = input_data.split(" ")
    command, filename, *args  = input_data
    assert subprocess.check_output([command, filename, *args], encoding="cp1251").strip().replace("\r", "") == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['file_search'])
def test_file_search(input_data, expected):
    input_data = input_data.split(" ")
    command, filename, *args  = input_data
    assert subprocess.check_output([command, filename, *args], encoding="cp1251").strip().replace("\r", "") == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['email_validation'])
def test_email_validation(input_data, expected):
    assert run_script('email_validation.py', [input_data]) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['fibonacci'])
def test_fibonacci(input_data, expected):
    assert run_script('fibonacci.py', [input_data]) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['compute_average_scores'])
def test_compute_average_scores(input_data, expected):
    assert run_script('average_scores.py', [input_data]) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['phone_number'])
def test_phone_number(input_data, expected):
    assert run_script('phone_number.py', [input_data]) == expected
