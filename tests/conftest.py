import pytest 
import os
@pytest.fixture

def txt_archive():
    #It returns the given path of the txt file
    #/Users/benjavitale/Documents/GitHub/TP-Final/tests/test_texfile.txt
    #/Users/benjavitale/Documents/GitHub/TP-Final/tests/test_texfile-1.txt
    return os.path.abspath('test_texfile-1.txt')