# Copyright (c) 2021 Itz-fork

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 1234567))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    DOWNLOAD_LOCATION = "./NexaBots"
    IS_PUBLIC_BOT = os.environ.get("IS_PUBLIC_BOT", "False")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", -1234567))
    TG_MAX_SIZE = 2040108421
    # Mega User Account
    MEGA_EMAIL = os.environ.get("MEGA_EMAIL", "")
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD", "")

# Text Prints
B_START_TEXT = """
I am Megadl Bot By @Tellybots_4u

Process: {}
"""

PROCESS_TEXT = """
Process: {}
"""

LOGGED_AS_USER = """
Successfully Logged Into Mega.nz User Account
"""

LOGIN_ERROR_TEXT = """
Can't Get Mega Email and Password Login as an Anonymous User
"""

ERROR_TEXT = """
An Expected Error Occurred

Log: {}

Save the Log file and Send it to @Tellybots_4u for Help :)
"""

START_TEXT="""
Hi {}\n\nI am Mega-dl Bot\n\nI can help You to download files from Mega web
Made with 💕 By @Tellybots_4u
"""
