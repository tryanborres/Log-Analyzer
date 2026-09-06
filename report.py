# Generates the output report
from colorama import init, Fore, Style

init()

def display_results(flagged_events, brute_force_attempts):
    """
    Prints a formatted summary of all flagged events and brute force attempts
    to the terminal with color coded severity levels.
    Shows total counts for each severity level at the end.
    """
    pass

def save_report(flagged_events, brute_force_attempts, filename):
    """
    Saves the full analysis report to a text file.
    Includes:
        - scan timestamp
        - total events analyzed
        - all flagged events with severity and description
        - any detected brute force attempts
    """
    pass