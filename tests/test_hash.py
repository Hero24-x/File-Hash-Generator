from core.hasher import generate_hashes

def test_hash():
    result = generate_hashes("sample.txt")
    assert "MD5" in result
    assert "SHA1" in result
    assert "SHA256" in result
