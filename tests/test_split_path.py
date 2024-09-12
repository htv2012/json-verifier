from json_verifier import JsonVerifier


def test_split_default():
    verifier = JsonVerifier({})
    assert verifier.split_path("a.b.c") == ["a", "b", "c"]


def test_split_non_default():
    verifier = JsonVerifier({}, separator="/")
    assert verifier.split_path("a/b.c/d") == ["a", "b.c", "d"]
