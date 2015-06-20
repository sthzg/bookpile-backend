#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    from settings.utils import get_env_variable
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.{}".format(
        get_env_variable('DJ_PROJECT_CURRENT_ENV')))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
