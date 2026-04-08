#!/usr/bin/env python
"""
Django Admin Utility Script
---------------------------
This script allows you to run administrative tasks for the Student_Management project.

Pull Request Enhancements:
- Added better error handling
- Added optional logging
- Included environment variable validation
"""

import os
import sys
import logging

# Set up logging (Optional debug output)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Run Django administrative tasks."""
    # Set default settings module if not already set
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Student_Management.settings')

    # Validate environment setup
    if 'DJANGO_SETTINGS_MODULE' not in os.environ:
        logger.error("DJANGO_SETTINGS_MODULE is not set.")
        sys.exit(1)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        logger.exception("Django import failed.")
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    logger.info("Starting Django administrative command...")
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
