from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class10/collateral/detect_platform.py",
    "../class10/collateral/snmp_detect.py",
    "../class10/collateral/telnet_example.py",
    "../class10/collateral/write_read.py",
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


def test_class10_ex1():
    base_path = "../class10/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("cisco_xe") == 2
    assert std_out.count("cisco_nxos") == 2
    assert std_out.count("juniper_junos") == 2


def test_class10_ex2():
    base_path = "../class10/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("cisco_xe") == 2
    assert std_out.count("cisco_nxos") == 2
    assert std_out.count("juniper_junos") == 2
    assert "Creating devices.yaml file" in std_out


def test_class10_ex3():
    base_path = "../class10/exercises/"
    cmd_list = ["python", "exercise3.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("cisco3") == 3
    assert "Trying 10.220.88.22" in std_out
