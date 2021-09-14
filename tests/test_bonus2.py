from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../bonus2/collateral/log_only/conn_log.py",
    "../bonus2/collateral/send_multiline/mline_pattern.py",
    # "../bonus2/collateral/send_multiline/file_delete_pattern.py",
    # "../bonus2/collateral/send_multiline_timing/file_delete_timing.py",
    "../bonus2/collateral/send_multiline_timing/mline_time.py",
]

TEST_COLLATERAL_EXC = []


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


def test_bonus2_ex1():
    base_path = "../bonus2/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Target IP" in std_out
    assert "8.8.8.8" in std_out
    assert std_out.count("!") >= 180


def test_bonus2_ex2():
    base_path = "../bonus2/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Target IP" in std_out
    assert "8.8.8.8" in std_out
    assert std_out.count("!") >= 180


def test_bonus2_ex3():
    base_path = "../bonus2/exercises/"
    cmd_list = ["python", "exercise3.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Target IP" in std_out
    assert "8.8.8.8" in std_out
    assert std_out.count("!") >= 90
    assert "cisco3" not in std_out
    assert "cisco4" in std_out
