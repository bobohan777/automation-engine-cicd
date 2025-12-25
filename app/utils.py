"""
Utility functions for Automation Engine
"""

from datetime import datetime
from typing import Any, Dict


def validate_input(data: Any) -> bool:
    """
    Validate input data

    Args:
        data: Input data to validate

    Returns:
        bool: True if valid, False otherwise
    """
    if data is None:
        return False

    if isinstance(data, dict) and len(data) == 0:
        return False

    return True


def format_response(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format API response with standard structure

    Args:
        data: Response data

    Returns:
        dict: Formatted response
    """
    return {
        "success": "error" not in data,
        "data": data,
        "timestamp": datetime.utcnow().isoformat(),
    }


def sanitize_string(input_string: str) -> str:
    """
    Sanitize input string

    Args:
        input_string: String to sanitize

    Returns:
        str: Sanitized string
    """
    if not isinstance(input_string, str):
        return ""

    # Remove potentially dangerous characters
    dangerous_chars = ["<", ">", "&", '"', "'"]
    sanitized = input_string

    for char in dangerous_chars:
        sanitized = sanitized.replace(char, "")

    return sanitized.strip()


def calculate_uptime(start_time: datetime) -> str:
    """
    Calculate uptime from start time

    Args:
        start_time: Application start time

    Returns:
        str: Formatted uptime string
    """
    uptime = datetime.utcnow() - start_time
    days = uptime.days
    hours, remainder = divmod(uptime.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{days}d {hours}h {minutes}m {seconds}s"
