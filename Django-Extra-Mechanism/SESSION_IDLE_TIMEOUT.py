# SESSION IDLE TIMEOUT IN DJANGO

# Added following lines in “settings.py” of your project.

SESSION_COOKIE_AGE = 60 * 30  # Session will expiry after 30 minutes idle.
SESSION_SAVE_EVERY_REQUEST = True