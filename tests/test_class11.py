from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class11/collateral/term_server1.py",
    "../class11/collateral/term_server2.py",
    "../class11/collateral/term_server3.py",
    "../class11/collateral/term_server4.py",
    "../class11/collateral/redispatch1.py",
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
