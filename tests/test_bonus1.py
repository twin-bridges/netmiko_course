import time
from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../bonus1/collateral/send_command/traceroute_working.py",
    "../bonus1/collateral/send_command_timing/traceroute_working.py",
]

TEST_COLLATERAL_EXC = [
    "../bonus1/collateral/send_command/traceroute_timeout.py",
    "../bonus1/collateral/send_command/traceroute_long.py",
    "../bonus1/collateral/send_command_timing/traceroute_timeout.py",
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


@pytest.mark.parametrize("test_case", TEST_COLLATERAL_EXC)
def test_runner_collateral_exception(test_case):

    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 1
    assert "raise ReadTimeout" in std_err


def test_bonus1_ex1():
    base_path = "../bonus1/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Program failed" in std_out
    assert "Execution time" in std_out
    # Let show tech-support complete
    time.sleep(120)


def test_bonus1_ex2():
    base_path = "../bonus1/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Resource" in std_out
    assert "Execution time" in std_out


def test_bonus1_ex3():
    base_path = "../bonus1/exercises/"
    cmd_list = ["python", "exercise3.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Resource" in std_out
    assert "Exec time" in std_out
