class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    image = str(body.get("image", ""))
    if image.endswith(":latest") or image == "latest":
        failed.append("image_tag_latest")

    if not body.get("alias"): failed.append("missing_alias")\n    if not body.get("tests_passed"): failed.append("tests")
    return {"passed": not failed, "failed": failed, "applied": False}
