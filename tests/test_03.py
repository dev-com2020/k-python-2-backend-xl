from unittest.mock import Mock


def send_email():
    print("Sending emial")


def test_send_email():

    mock_mail = Mock()
    mock_mail()
    mock_mail.send_email.return_value = True
    result = mock_mail.send_email()

    assert result is True
    mock_mail.assert_called()