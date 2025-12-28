from json_verifier import JsonVerifier


def test_that_failed():
    # A value we want to test
    actual = {
        "meta": {
            "id": 501,
            "description": "A test thing",
        },
    }

    verifier = JsonVerifier(actual)
    with verifier:
        verifier.verify_value("meta.id", 1001)
        verifier.verify_value("meta.name", "My Object")
        verifier.verify_value(("meta", "description"), "A Test Object")
