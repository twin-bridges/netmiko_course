from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class3/collateral/show_textfsm.py",
    "../class3/collateral/show_genie.py",
    "../class3/collateral/show_genie_nxos.py",
    "../class3/collateral/show_ttp.py",
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


def test_class3_ex1():
    base_path = "../class3/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "VLAN ID: 7" in std_out
    assert "VLAN0007" in std_out


def test_class3_ex2():
    base_path = "../class3/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("nxos2") == 4
    assert std_out.count("10.0.2.16") == 4


def test_class3_ex3():
    base_path = "../class3/exercises/"
    cmd_list = ["python", "exercise3.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "VLAN ID: 7" in std_out
    assert "VLAN0007" in std_out
