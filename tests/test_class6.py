from pathlib import Path
import pytest
import os
import subprocess

from utilities import subprocess_runner


def run_ssh_agent():
    # Check for already running ssh-agent
    cmd_list = ["ps", "auwx"]
    # cmd_list = "ps auwx | grep ssh-agent | grep -v grep"
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=".")
    ssh_agent_running = False
    for line in std_out.splitlines():
        if "ssh-agent" in line:
            if "grep" in line:
                continue
            else:
                ssh_agent_running = True
                break

    # Retrieve the current environment
    env = os.environ.copy()
    if not ssh_agent_running:
        # Start the SSH Agent
        cmd_list = ["ssh-agent"]
        std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=".")

        # Set the environment variables
        for line in std_out.splitlines():
            if "SSH_AUTH_SOCK" in line or "SSH_AGENT_PID" in line:
                cmd_list = line.split(";")
                # Filter blank lines
                cmd_list = [cmd for cmd in cmd_list if cmd]
                for cmd in cmd_list:
                    if "=" in cmd:
                        env_var, env_value = cmd.split("=")
                        env[env_var] = env_value
                        break

    # And ssh-add ~/.ssh/test_rsa
    cmd_list = ["ssh-add", "~/.ssh/test_rsa"]
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, shell=True
    ) as proc:
        std_out, std_err = proc.communicate()
    print(std_err)

    cmd_list = ["ssh-add", "-l"]
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, shell=True
    ) as proc:
        std_out, std_err = proc.communicate()
    print(std_err)

    return env


TEST_COLLATERAL = [
    "../class6/collateral/ssh_keys.py",
    "../class6/collateral/ssh_keys_encr.py",
    "../class6/collateral/ssh_config_file.py",
    "../class6/collateral/ssh_proxy_jump.py",
    # "../class6/collateral/ssh_keys_agent.py",
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


# Close, but not quite working :-(
# def test_ssh_agent():
#
#     # Setup the SSH Agent
#     env = run_ssh_agent()
#
#     test_case = "../class6/collateral/ssh_keys_agent.py"
#     path_obj = Path(test_case)
#     script = path_obj.name
#     script_dir = path_obj.parents[0]
#
#     cmd_list = ["python", script]
#     with subprocess.Popen(
#         cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, cwd=script_dir
#     ) as proc:
#         std_out, std_err = proc.communicate()
#     print(std_out)
#     print(std_err)
#     # assert return_code == 0
#     assert std_err == ""

def test_class6_ex1():
    base_path = "../class6/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("10.220.88.1 ") == 2


# Will fail in the lab environment as things are missing (SSH keyfile, SSH trust)
#def test_class6_ex3():
#    base_path = "../class6/exercises/"
#    cmd_list = ["python", "exercise3.py"]
#    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
#    assert return_code == 0
#    assert std_err == ""
#    assert std_out.count("Line") == 1
#    assert std_out.count("Location") == 1
