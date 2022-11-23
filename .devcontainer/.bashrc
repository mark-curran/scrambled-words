# ~/.bashrc: executed by bash(1) for non-login shells.

# Note: PS1 and umask are already set in /etc/profile. You should not
# need this unless you want different defaults for root.
# PS1='${debian_chroot:+($debian_chroot)}\h:\w\$ '
# umask 022

# You may uncomment the following lines if you want `ls' to be colorized:
# export LS_OPTIONS='--color=auto'
# eval "$(dircolors)"
# alias ls='ls $LS_OPTIONS'
# alias ll='ls $LS_OPTIONS -l'
# alias l='ls $LS_OPTIONS -lA'
#
# Some more alias to avoid making mistakes:
# alias rm='rm -i'
# alias cp='cp -i'
# alias mv='mv -i'

# Enable git prompt.
source ~/.git-prompt.sh
GIT_PROMPT_COMMAND='__git_ps1 "\[\033[01;32m\]\u@\h:\[\033[01;34m\]\w\[\033[01;31m\]" "\\[\033[00m\]\$ "'
# Enable git command completion:
source ~/.git-completion.bash

# Write to the history file after every command
HISTORY_PROMPT_COMMAND='history -a'
# Set location of command history file.
export HISTFILE=/root/.bash_history

# Set the prompt command
export PROMPT_COMMAND="${HISTORY_PROMPT_COMMAND} && ${GIT_PROMPT_COMMAND}"
