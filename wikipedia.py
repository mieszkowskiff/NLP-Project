import wikipediaapi

def wiki_wiki() -> wikipediaapi.Wikipedia:
    """
    This function returns the wikipedia object.
    :return: wikipediaapi.Wikipedia: The wikipedia object.
    """
    return wikipediaapi.Wikipedia("Turboprojekt na NLP",  "en") 

def get_section_text(page_title: str, section_title: str, wiki_wiki = None) -> str:
    """
    This function returns the text of the page from the title.
    :param title: str: The title of the page.
    :return: str: The text of the page.
    """
    if wiki_wiki is None:
        wiki_wiki = wikipediaapi.Wikipedia("Turboprojekt na NLP",  "en")
    page = wiki_wiki.page(page_title)
    section = page.section_by_title(section_title)
    return section.text

titles_to_remove = [
    "References", 
    "External links", 
    "See also", 
    "Further reading", 
    "Notes",
    "Sources",
    "Gallery",
    "Citations"
]

def get_section_titles(page_title: str, wiki_wiki = None) -> list[str]:
    """
    This function returns the section names of the page from the title.
    :param title: str: The title of the page.
    :return: list[str]: The section names of the page.
    """
    if wiki_wiki is None:
        wiki_wiki = wikipediaapi.Wikipedia("Turboprojekt na NLP",  "en")
    page = wiki_wiki.page(page_title)
    titles = [section.title for section in page.sections]
    for title_to_remove in titles_to_remove:
        if title_to_remove in titles:
            titles.remove(title_to_remove)
    return titles


if __name__ == "__main__":
    wiki = wiki_wiki()
    print(wiki.page("Nute Gunray").exists())
    print(get_section_titles("Nute Gunray", wiki))


