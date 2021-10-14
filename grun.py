import os

def create_tmux_session(session):
    os.system(f"tmux has-session -t {session} || tmux new-session -d -A -s {session}")
    print(f'To access local tmux session: tmux attach-session -t {session}')

def create_remote_session(remote_session):
    send_to_tmux('main', f'tmux has-session -t {remote_session} || tmux new-session -d -A -s {remote_session}')

def log_onto_tpu_vm(session, tpu_vm, zone='us-central1-f', project='subgoal-search-atp'):
    send_to_tmux(session, f'gcloud alpha compute tpus tpu-vm ssh {tpu_vm} --zone {zone} --project {project}')

def kill_tmux_session(session):
    os.system(f"tmux kill-session -t {session}")

def send_to_tmux(session, content):
    os.system(f"tmux send-keys -t {session}:0 '{content}' Enter")

def send_to_remote_tmux(session, remote_session, content):
    print(f"tmux send-keys -t {remote_session}:0 '{content}'")
    # assert False
    send_to_tmux(session, f"tmux send-keys -t {remote_session}:0 '{content}'")


LOCAL_SESSION = 'main'
REMOTE_SESSION = 'remote_main'

create_tmux_session(LOCAL_SESSION)

create_remote_session(REMOTE_SESSION)

# os.system("tmux new-session -d -A -s main")
# os.system("tmux send-keys -t main:0 'echo dupa > duuuupa.txt' Enter")
#
# send_to_tmux('main', 'gcloud alpha compute tpus tpu-vm ssh tpu-us --zone us-central1-f --project subgoal-search-atp')
# send_to_remote_tmux('main', 'remote_main', 'echo wielka_dupa')
# send_to_tmux('main', 'logout')
# kill_tmux_session(LOCAL_SESSION)

#
# os.system("tmux send-keys -t main:0 'gcloud alpha compute tpus tpu-vm ssh tpu-us --zone us-central1-f --project subgoal-search-atp' Enter")
# os.system("tmux send-keys -t main:0 'python3 hi.py' Enter")