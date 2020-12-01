from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class8/collateral/cf_threads.py",
    "../class8/collateral/cf_threads_asc.py",
    "../class8/collateral/cf_processes.py",
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
