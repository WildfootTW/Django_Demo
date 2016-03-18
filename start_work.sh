tmux split-window -h
tmux split-window -h
#tmux select-pane -t 2
#source ./venv/bin/activate
tmux kill-pane -t 1
tmux select-pane -t 0
source ./venv/bin/activate
tmux split-window -d
tmux select-pane -t 1
#source ./venv/bin/activate

