import os
import subprocess

from SHH_configuration import REMOTES

def create_tmux_session(session_name):
    print(f'Creating a remote tmux session. To attach: tmux attach-session -t {session_name}')
    return f'tmux has-session -t {session_name} || tmux new-session -d -A -s {session_name}'

def create_command_to_tmux(session_name, command):
    return f"tmux send-keys -t {session_name}:0 '{command}' Enter"

def send_command_to_remote(remote, command):
    command_output = subprocess.run(f'ssh {REMOTES[remote]} "{command}"', shell=True, capture_output=True)
    # print(command_output)
    return command_output

def create_remote_tmux_session(remote, session_name):
    send_command_to_remote(remote, create_tmux_session(session_name))

def send_command_to_remote_tmux(remote, session_name, command):
    send_command_to_remote(remote, create_command_to_tmux(session_name, command))

def transfer_directory(remote, local_path, remote_path):
    subprocess.run(f'rsync -avz --exclude cluster_runner {local_path}/ {REMOTES[remote]}:{remote_path}/', shell=True)


# send_command_to_remote(1, 'tmux')

create_remote_tmux_session(1, 'wielki_duper_sesja')
# transfer_directory(1, 'wielki_duper_sesja', 'example_pythons', 'to_i_owo')
# send_command_to_remote_tmux(1, 'wielki_duper_sesja', 'python3 hi.py')


# def create_tmux_session(session_name):
#     print(f'Creating a remote tmux session. To attach: tmux attach-session -t {session_name}')
#     return f'tmux has-session -t {session_name} || tmux new-session -d -A -s {session_name}'
#
# def create_command_to_tmux(session_name, command):
#     return f"tmux send-keys -t {session_name}:0 '{command}' Enter"
#
# def send_command_to_remote(remote, command):
#     subprocess.run
#     os.system(f'ssh {REMOTES[remote]} "{command}"')
#
# def create_remote_tmux_session(remote, session_name):
#     send_command_to_remote(remote, create_tmux_session(session_name))
#
# def send_command_to_remote_tmux(remote, session_name, command):
#     send_command_to_remote(remote, create_command_to_tmux(session_name, command))
#
# def transfer_directory(remote, session_name, local_path, remote_path):
#     os.system(f'rsync -avz --exclude cluster_runner {local_path}/ {REMOTES[remote]}:{remote_path}/')
