import related
from .models import Settings

original_yaml = """
devices:
    left-keyboard:  000123456789
    right-keyboard: 000987654321
"""


def test_self_reference():
    root_node = related.from_yaml(original_yaml, Settings)

    assert root_node.devices['left-keyboard'] == "000123456789"
    assert root_node.devices['right-keyboard'] == "000987654321"
