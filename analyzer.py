# Flags suspicious activity and assigns severity levels
from colorama import init, Fore, Style

init()

# Windows Event IDs we care about and what they mean
SUSPICIOUS_EVENT_IDS = {
    4625: {"description": "Failed login attempt",           "severity": "medium"},
    4648: {"description": "Login with explicit credentials","severity": "medium"},
    4672: {"description": "Admin privileges assigned",      "severity": "high"},
    4698: {"description": "Scheduled task created",         "severity": "high"},
    4719: {"description": "Audit policy changed",           "severity": "critical"},
    4720: {"description": "User account created",           "severity": "high"},
    4726: {"description": "User account deleted",           "severity": "high"},
    4732: {"description": "User added to admin group",      "severity": "critical"},
    4740: {"description": "Account locked out",             "severity": "high"},
    4756: {"description": "Member added to security group", "severity": "high"},
    7045: {"description": "New service installed",          "severity": "critical"},
}

def analyze_events(parsed_events):
    """
    Loops through all parsed events and flags any that match our suspicious
    Event ID list. Assigns a severity level to each flagged event.
    Returns a list of flagged events with their severity levels.
    """
    pass

def detect_brute_force(parsed_events, threshold=5):
    """
    Detects brute force login attempts by counting failed logins (Event ID 4625)
    from the same IP address or username within the log.
    If the count exceeds the threshold (default 5), it flags it as a brute force attempt.
    Returns a list of detected brute force attempts.
    """
    pass

def assign_severity_color(severity):
    """
    Returns a color coded severity label using colorama.
    Severity levels:
        low      = green
        medium   = yellow
        high     = red
        critical = bright red
    """
    pass