"""
Basic test for version consistency.
"""

import fusionaize_docs

def test_version_exists() -> None:
    """Ensure __version__ is defined."""
    assert hasattr(fusionaize_docs, "__version__")
    assert isinstance(fusionaize_docs.__version__, str)
    assert len(fusionaize_docs.__version__) > 0