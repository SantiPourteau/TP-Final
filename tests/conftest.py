import pytest 
import os
@pytest.fixture
def txt_archive():
    #It returns the given path of the txt file
   
    return os.path.abspath(os.path.join('tests','test_texfile-1.txt'))
