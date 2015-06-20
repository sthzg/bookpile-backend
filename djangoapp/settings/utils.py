# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))


def get_env_variable(var_name, default=False):
    """ Gets the environment variable or return exception.

    :param var_name: Environment Variable to lookup
    """
    try:
        return os.environ[var_name]
    except KeyError:
        try:
            from io import StringIO
        except ImportError:
            from six import StringIO
        try:
            import configparser
        except ImportError:
            from six.moves import configparser

        env_file = os.environ.get(
            'PROJECT_ENV_FILE',
            os.path.abspath(os.path.join(BASE_DIR, "../env/env_vars/.env"))
        )

        try:
            config = StringIO()
            config.write("[DATA]\n")
            config.write(open(env_file).read())
            config.seek(0, os.SEEK_SET)
            cp = configparser.ConfigParser()
            cp.readfp(config)
            value = dict(cp.items('DATA'))[var_name.lower()]
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            os.environ.setdefault(var_name, value)
            return value

        except (KeyError, IOError):
            if default is not False:
                return default

            from django.core.exceptions import ImproperlyConfigured
            error_msg = (
                "Either set the env variable '{var}' or place it in your "
                "{env_file} file as '{var} = VALUE'"
            )

            raise ImproperlyConfigured(error_msg.format(
                var=var_name,
                env_file=env_file
            ))
