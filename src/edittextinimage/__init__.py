"""EditTextInImage — thin reference to the Edit Text In Image web tool."""

HOMEPAGE = "https://edittextinimage.com/"
SUPPORT_EMAIL = "support@edittextinimage.com"

def open_homepage() -> str:
    """Return the canonical product homepage URL."""
    return HOMEPAGE

__all__ = ["HOMEPAGE", "SUPPORT_EMAIL", "open_homepage"]
__version__ = "0.1.0"
