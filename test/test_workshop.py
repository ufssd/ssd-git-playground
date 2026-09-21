import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from workshop import get_bowl_status, get_menu_heading


def expect_equal(actual, expected, message):
    if actual != expected:
        print(f"FAIL: {message}")
        print(f"Expected: {expected}")
        print(f"Received: {actual}")
        sys.exit(1)


expect_equal(get_bowl_status(), "ready", "Bowl status should be ready")
expect_equal(get_menu_heading(), "Menu", "Menu heading should be named Menu")

print("All checks passed.")
