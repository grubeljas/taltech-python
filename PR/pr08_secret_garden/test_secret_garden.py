import pytest

from secret_garden import Decoder, SecretGarden

filename = "pr08_example_data.txt"
key = "Fat Chocobo"
d = Decoder(filename, key)
sg = SecretGarden(filename, key)


def test_decode():

    assert len(d.decode()) == 7
    assert d.decode()[0] == "-12;-1\n\nESS"
    assert d.decode()[1] == "19;-14\n\nNEWNESSEWN"
    assert sg.decode_messages()[0] == "-12;-1\n\nESS"
    assert d.decode_from_base64('MDsyCgpOTlNXV0U=') == '0;2\n\nNNSWWE'
    assert d.calculate_cipher_step() == 1016
    assert d.read_code_from_file() == ['KS0uNyktBgZBT08=', 'LTU3KS0wBgZKQVNKQU9PQVNK', 'KTA3KTIGBkFKU0FKQUpPQUpKQUFP', 'LjcpLwYGQUpTU0FKU0pPT1NTT09PUw==', 'LSw3MAYG', 'LDcpLSwGBk9BQVNTT1NPQUFBU0FBQUFB', 'LjcpLgYGU09TQU9KQU9PTw==']
    assert d.key == key
    assert d.file == filename
    assert sg.file == filename
    assert sg.key == key
    assert sg.find_secret_locations() == [(-11, -3), (20, -13), (1, -3), (-2, -5), (10, 4), (6, -13), (2, -6)]
