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
    for ch in item.select(chapter_selector):
        ch_link = ch.select_one(link_selector)
        if ch_link:
            chapters.append({
                "chapter": ch_link.text.strip(),
                "url": ch_link["href"]
            })
    return chapters