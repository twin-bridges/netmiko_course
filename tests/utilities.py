import subprocess


def subprocess_runner(cmd_list, exercise_dir):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=exercise_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


def subprocess_runner_stdin(cmd_list, stdin_responses, exercise_dir):
    """Wrapper to execute subprocess including handling stdin."""
    if isinstance(stdin_responses, list):
        stdin_responses = "\n".join(stdin_responses)

    # universal_newlines will cause it to accept and return strings, not bytes
    proc = subprocess.Popen(
        cmd_list,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,
        universal_newlines=True,
        cwd=exercise_dir,
    )
    std_out, std_err = proc.communicate(input=stdin_responses)
    return (std_out, std_err, proc.returncode)
