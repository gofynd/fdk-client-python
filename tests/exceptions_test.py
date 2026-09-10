from fdk_client.common.exceptions import FDKTokenIssueError


def test_fdk_token_issue_error_init():
    err = FDKTokenIssueError("test message")
    assert str(err) == "test message"
