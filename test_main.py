# Code pour tester la fonction miroir du main
from main import miroir_str
import pytest

def test_miroir_str():
    # Ce test réussira
    assert miroir_str('abc') == 'cba'
