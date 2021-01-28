from pathlib import Path
import pytest
import time

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class5/collateral/config_vlans.py",
    "../class5/collateral/config_file.py",
    "../class5/collateral/disable_cmd_verify.py",
    # "../class5/collateral/config_rm_user.py",
]


@pytest.mark.parametrize("test_case", TEST_COLLATERAL)
def test_runner_collateral(test_case):
    # Arista's seem to have an issue where device's get overloaded?
    time.sleep(3)
    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    print(std_err)
    assert return_code == 0
    assert std_err == ""
    assert "Traceback" not in std_out


def test_class5_ex1():
    base_path = "../class5/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("ip domain-lookup") == 2
    assert std_out.count("ip domain-name bogus.com") == 2


def test_class5_ex2():
    base_path = "../class5/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("vlan 501") == 2
    assert std_out.count("vlan 502") == 2


def test_class5_ex3():
    base_path = "../class5/exercises/"
    cmd_list = ["python", "exercise3.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Changing the terminal width" in std_out
    assert "Setting the hostname to a very long value" in std_out
    assert "Testing long command that should now fail" in std_out
    assert "long command failed with an exception" in std_out
    assert std_out.count("show ip interface brief vrf management | include manage") == 2
    assert "Restoring hostname to original value" in std_out
