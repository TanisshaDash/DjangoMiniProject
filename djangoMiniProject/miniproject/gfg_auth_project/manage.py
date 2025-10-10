import os
import sys
from dotenv import load_dotenv  # make sure to install python-dotenv

def main():
    """Run administrative tasks."""
    load_dotenv()  # load variables from .env file

    # Allow HTTP OAuth in dev only
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = os.getenv('OAUTHLIB_INSECURE_TRANSPORT', '0')

    # Point to your credentials file securely
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
