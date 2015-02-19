#!/usr/bin/env python
"""
Command-line utility for administrative tasks.
"""

import os
import sys
sys.path.append('D:\MyDocs\Documents\Visual Studio 2013\Projects\SE3800Project\SE3800Project\env\Lib\site-packages')

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "SE3800Project.settings"
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
