from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class9/collateral/get_file.py",
    "../class9/collateral/get_progress_bar.py",
    "../class9/collateral/put_file.py",
    "../class9/collateral/put_progress_bar.py",
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


def test_class9_ex1():
    base_path = "../class9/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("Name servers are correct") == 2
    assert std_out.count("Domain name is correct") == 2


def test_class9_ex2():
    base_path = "../class9/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Redirecting" in std_out
    assert "Verifying" in std_out
    assert "Retrieving" in std_out
    assert "file successfully transferred" in std_out
