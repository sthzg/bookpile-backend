#!/bin/bash
# Example crontab:
# */1 * * * * /path/to/stack_check.sh >> $HOME/logs/cron/cron_stack_check.log 2>&1
export PATH=/sbin:$PATH
if pidof -x supervisord; then
    echo 'Systems are running.'
else
    date
    echo 'Systems need to be rebooted.'
    /path/to/python {{ supervisor_bin_path }}/supervisord -c {{ supervisor_conf_path }}/supervisord.ini
fi