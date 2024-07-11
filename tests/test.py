from pathlib import Path
from dot_slash import dot_slash

def test_get_contents():
    contents = Path(dot_slash("stuff.txt")).read_text()
    assert contents == "yep, these are the contents"
