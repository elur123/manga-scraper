## /search

```json
{
    "url": "https://harimanga.me/?s=killer&post_type=wp-manga",
    "page": 1,
    "item_selector": ".c-tabs-item__content",
    "title_selector": ".post-title a",
    "rating_selector": ".post-total-rating span",
    "thumbnail_selector": ".c-image-hover img",
    "status_selector": ".summary-content",
    "latest_chapter": ".latest-chap .chapter a",
    
}
```

## /categories

```json
{
    "url": "https://harimanga.me",
    "item_selector": ".menu-item-object-wp-manga-genre",
    "title_selector": "a"
}
```

## /recent

```json
{
    "url": "https://harimanga.me",
    "page": 1,
    "item_selector": ".page-item-detail",
    "title_selector": ".post-title a",
    "rating_selector": ".post-total-rating span",
    "thumbnail_selector": ".item-thumb img",
    "chapter_selector": ".chapter-item",
    "chapter_link_selector": "a.btn-link"
}
```

## /popular

```json
{
    "url": "https://harimanga.me",
    "item_selector": ".popular-item-wrap",
    "title_selector": ".widget-title a",
    "thumbnail_selector": ".popular-img img",
    "chapter_selector": ".chapter-item",
    "chapter_link_selector": "a.btn-link"
}
```

## /manga-details

```json
{
    "url": "https://harimanga.me/manga/let-me-enjoy-the-extra-life/",
    "title_selector": ".post-title h1",
    "thumbnail_selector": ".summary_image img",
    "description_selector": ".summary__content",
    "chapters_selector": ".wp-manga-chapter a",
    "status_selector": ".summary-content"
}
```

## /manga-read

```json
{
    "url": "https://harimanga.me/manga/let-me-enjoy-the-extra-life/chapter-45/",
    "image_selector": ".page-break img"
}
```