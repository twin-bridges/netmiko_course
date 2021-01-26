from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class4/collateral/multiline_prompt.py",
    "../class4/collateral/show_w_delay.py",
    "../class4/collateral/multiline_timing.py",
]


@pytest.mark.parametrize("test_case", TEST_COLLATERAL)
def test_runner_collateral(test_case):
    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 0
    assert std_err == ""
    assert "Traceback" not in std_out


def test_class4_ex1():
    base_path = "../class4/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "copy flash" in std_out
    assert "Copy in progress" in std_out
    assert "bytes copied" in std_out


def test_class4_ex2():
    base_path = "../class4/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "copy flash" in std_out
    assert "Copy in progress" in std_out
    assert "bytes copied" in std_out


def test_class4_ex3():
    base_path = "../class4/exercises/"
    cmd_list = ["python", "exercise3.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Case1" in std_out
    assert "Case2" in std_out
    assert "Case3" in std_out
    assert "Case4" in std_out
    assert std_out.count("cisco3#") == 4


def test_class4_ex4():
    base_path = "../class4/exercises/"
    cmd_list = ["python", "exercise4.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Building configuration..." in std_out
    assert "Current configuration" in std_out
    assert "Execution Time" in std_out
