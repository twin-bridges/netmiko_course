import re
from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class12/collateral/fast_cli.py",
    "../class12/collateral/enable.py",
    "../class12/collateral/config_mode.py",
    "../class12/collateral/commit.py",
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


def test_class12_ex1():
    base_path = "../class12/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 1
    assert "ReadTimeout" in std_err
    assert "Fast CLI state" in std_out
    assert "Global Delay Factor state" in std_out
    assert "Command execution time" in std_out


def test_class12_ex2():
    base_path = "../class12/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("cisco4") == 3
    assert re.search(r"cisco4.*\(config\)#", std_out)
    assert "cisco4-testing#" in std_out


def test_class12_ex3():
    base_path = "../class12/exercises/"
    cmd_list = ["python", "exercise3.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Send configuration commands to device" in std_out
    assert "Commit change...operation is slow" in std_out
    assert "commit complete" in std_out
    assert "Configuration change using Netmiko (ktb)" in std_out
