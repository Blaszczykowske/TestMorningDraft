from main import check_website_status

def test_website_status():
    print("[test_main.py] Running test_website_status...")
    title = check_website_status()
    assert title is not None, "Website did not load or title not found"
    assert "Morning Draft" in title or "morningdraft" in title.lower(), "Unexpected website title"