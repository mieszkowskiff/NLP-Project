import wikipediaapi


def get_section_text(page_title: str, section_title: str) -> str:
    """
    This function returns the text of the page from the title.
    :param title: str: The title of the page.
    :return: str: The text of the page.
    """
    wiki_wiki = wikipediaapi.Wikipedia("Turboprojekt na NLP",  "en")
    page = wiki_wiki.page(page_title)
    section = page.section_by_title(section_title)
    return section.text


if __name__ == "__main__":
    print(len(get_section_text("Python (programming language)", "Design philosophy and features")))