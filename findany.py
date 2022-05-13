
class Keyword:
    """
    Search keywords in soup html
    """
    def __init__(self, soup, word):
        self.word = word
        self.soup = soup

    def find(self):
        # Find html's a elements that have :word: lambda text as lower case
        tags = self.soup.find_all('a',
                                  text=lambda t: t and self.word in t.lower()
                                  )

        for tag in tags:
            # If start with h menas it is a link. http.
            # Avoid menus or page structure links
            if tag['href'][0] == 'h':
                return tags
        return False

    # This method will be implemented in
    # next version after code institute evaluation
    def find_by(self, element):
        tags = self.soup.find_all(element, text=lambda t: t and self.word in t)
        last_tag = None
        for tag in tags:
            if last_tag != tag.text:
                print(f"\nFound: {tag.text}")
                last_tag = tag.text
