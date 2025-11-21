from urllib.parse import urlparse, parse_qs, urlencode

def extract_title(item, selector):
    tag = item.select_one(selector)
    if tag:
        return {"text": tag.text.strip(), "url": tag["href"]}
    return {"text": None, "url": None}

def extract_thumbnail(item, selector):
    img_tag = item.select_one(selector)
    return img_tag["src"] if img_tag else None

def extract_chapters(item, chapter_selector, link_selector):
    chapters = []
    # Select ALL chapter links inside chapter-item
    chapter_links = item.select(f"{chapter_selector} {link_selector}")

    for ch_link in chapter_links:
        based_url = ch_link["href"]
        slug = extract_slug(based_url, 1)
        chapter = extract_slug(based_url, -1)

        chapters.append({
            "chapter": ch_link.text.strip(),
            "url": based_url,
            "slug": slug,
            "chapter_slug": chapter
        })

    return chapters

def extract_url_scheme(base_url):
    parsed = urlparse(base_url)

    # Extract query parameters
    query_params = parse_qs(parsed.query)

    # Rebuild query string
    query = urlencode(query_params, doseq=True)

    return {
        "scheme": parsed.scheme,
        "netloc": parsed.netloc,
        "path": parsed.path,
        "query": query
    }

def extract_slug(base_url, index = -1):
    scheme = extract_url_scheme(base_url)
    return scheme["path"].strip("/").split("/")[index]