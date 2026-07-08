import pytest

from torana.core.plugin import Plugin


def test_plugin_is_abstract():

    with pytest.raises(TypeError):
        Plugin()