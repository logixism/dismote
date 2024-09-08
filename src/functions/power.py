from subprocess import run

def shutdown(delay: int = 0):
    run(['shutdown', '-s', '-t', str(delay)], capture_output=True)

def restart(delay: int = 0):
    run(['shutdown', '-r', '-t', str(delay)], capture_output=True)

def lock():
    run(['rundll32', 'user32.dll, LockWorkStation'], capture_output=True)

def rs_cancel():
    run(['shutdown', '-a'], capture_output=True)