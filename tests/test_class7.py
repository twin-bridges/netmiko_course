from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL_EXCEPT = [
    "../class7/collateral/tcp_conn_fail.py",
    "../class7/collateral/dns_fail.py",
    "../class7/collateral/auth_fail.py",
    "../class7/collateral/auth_fail_keys.py",
    # "../class7/collateral/banner_fail.py",
]

TEST_COLLATERAL = [
    "../class7/collateral/auth_retry.py",
    "../class7/collateral/auth_retry_func.py",
    "../class7/collateral/handle_failures.py",
]


@pytest.mark.parametrize("test_case", TEST_COLLATERAL_EXCEPT)
def test_runner_collateral_except(test_case):

    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 1
    assert "Traceback" in std_err


@pytest.mark.parametrize("test_case", TEST_COLLATERAL)
def test_runner_collateral(test_case):

    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 0
    assert std_err == ""
