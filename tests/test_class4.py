from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class4/collateral/send_command_prompting.py",
    "../class4/collateral/send_command_timing_prompting.py"
    "../class4/collateral/send_multiline/mline_pattern.py",
    # "../class4/collateral/send_multiline/file_delete_pattern.py",
    # "../class4/collateral/send_multiline_timing/file_delete_timing.py",
    "../class4/collateral/send_multiline_timing/mline_time.py",
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
    assert "Target IP" in std_out
    assert "8.8.8.8" in std_out
    assert std_out.count("!") >= 180


def test_class4_ex4():
    base_path = "../class4/exercises/"
    cmd_list = ["python", "exercise4.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Target IP" in std_out
    assert "8.8.8.8" in std_out
    assert std_out.count("!") >= 180
