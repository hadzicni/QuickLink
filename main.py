import pyshorteners

def shorten_url(long_url):
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url)
    
    return short_url

if __name__ == "__main__":
    long_url = input("Gib die lange URL ein, die du verkürzen möchtest: ")
    short_url = shorten_url(long_url)
    print("Die verkürzte URL ist:", short_url)
