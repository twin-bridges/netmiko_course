from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class2/collateral/netmiko_log.py",
    "../class2/collateral/conn_mult_devices.py",
    "../class2/collateral/show_command.py",
    "../class2/collateral/expect_str.py",
    "../class2/collateral/show_timing.py",
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


# def test_class1_ex1():
#     base_path = "../class1/exercises/exercise1/"
#     nornir_inventory = gen_inventory_dict(base_path)
#     nr = InitNornir(inventory=nornir_inventory, logging=NORNIR_LOGGING)
#     assert isinstance(nr, nornir.core.Nornir)
#     assert isinstance(nr.inventory.hosts, nornir.core.inventory.Hosts)
#     assert isinstance(nr.inventory.hosts["my_host"], nornir.core.inventory.Host)
#     assert nr.inventory.hosts["my_host"].hostname == "localhost"
