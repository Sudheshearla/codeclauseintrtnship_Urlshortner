import hashlib
import string
import random

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, long_url, size=6):
        hash_code = hashlib.sha256(long_url.encode()).hexdigest()
        short_code = self._generate_random_string(hash_code, size)
        short_url = f"http://short.url/{short_code}"  # Replace with your desired domain

        self.url_mapping[short_code] = long_url
        return short_url

    def _generate_random_string(self, hash_code, size):
        characters = string.ascii_letters + string.digits
        random.seed(hash_code)
        return ''.join(random.choice(characters) for _ in range(size))

if __name__ == "__main__":
    shortener = URLShortener()

    while True:
        long_url = input("Enter the long URL to shorten (or 'exit' to quit): ")
        if long_url.lower() == 'exit':
            break

        short_url = shortener.shorten_url(long_url)
        print(f"Short URL: {short_url}")

