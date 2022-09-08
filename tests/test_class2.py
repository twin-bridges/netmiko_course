import time
from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class2/collateral/netmiko_log.py",
    "../class2/collateral/conn_mult_devices.py",
    "../class2/collateral/show_command.py",
    "../class2/collateral/expect_str.py",
    "../class2/collateral/read_timeout/traceroute_working.py",
]

TEST_COLLATERAL_EXC = [
    "../class2/collateral/read_timeout/traceroute_timeout.py",
    "../class2/collateral/read_timeout/traceroute_long.py",
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


@pytest.mark.parametrize("test_case", TEST_COLLATERAL_EXC)
def test_runner_collateral_exception(test_case):

    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 1
    assert "raise ReadTimeout" in std_err


def test_class2_ex1():
    base_path = "../class2/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("10.220.88.1") == 4


def test_class2_ex2():
    base_path = "../class2/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "cisco3>" in std_out
    assert "cisco3#" in std_out


def test_class2_ex3():
    base_path = "../class2/exercises/"
    cmd_list = ["python", "exercise3.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Program failed" in std_out
    assert "Execution time" in std_out
    # Let show tech-support complete
    time.sleep(120)


def test_class2_ex4():
    base_path = "../class2/exercises/"
    cmd_list = ["python", "exercise4.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Resource" in std_out
    assert "Execution time" in std_out


# def test_class2_ex3():
#    base_path = "../class2/exercises/"
#    cmd_list = ["python", "exercise3.py"]
#    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
#    assert return_code == 0
#    assert std_err == ""
#    assert "cisco3>" in std_out
#    assert "cisco3#" in std_out
#    assert "cisco4>" in std_out
#    assert "cisco4#" in std_out
