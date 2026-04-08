from pages.google_page import GooglePage

def test_google(page):
    google = GooglePage(page)
    google.open()

    assert "Google" in google.get_title()