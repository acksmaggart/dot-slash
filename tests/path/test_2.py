from pathlib import Path
from dot_slash import dot_slash


def test_get_contents2():
    contents = Path(dot_slash("../stuff.txt")).read_text()
    assert contents == "yep, these are the contents"

    contents = Path(dot_slash("to/more_stuff.txt")).read_text()
    assert contents == "more stuff's contents"
