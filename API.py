import pandas as pd
import wikipedia


# def get_death_summary():
#     summary = wikipedia.summary("Death of Marilyn Monroe")
#     return summary

def fetch_summary(article):
    try:
        summary = wikipedia.summary(article, sentences=5)
        return summary
    except wikipedia.exceptions.PageError:
        return "\nCouldn't find page, please try to search again.\n"


def get_url(title):
    page = wikipedia.page(title, auto_suggest=False)
    return page.url


def get_address(article):
    page = wikipedia.WikipediaPage(article)
    page_content = page.content
    content_list = page_content.split()
    for index, word in enumerate(content_list):
        if article == "Los Angeles Police Department":
            if word == 'headquartered':
                return " ".join(content_list[index + 2: index + 11])
        elif article == "Death of Marilyn Monroe":
            if word == 'home' and content_list[index + 1] == 'at':
                return " ".join(content_list[index + 2: index + 11])
        elif article == "William Morris Agency":
            studio_house_number = '202 '
            if word == 'Canon':
                return studio_house_number + " ".join(content_list[index: index + 5])
        elif article == "20th Century Studios":
            url = get_url(article)
            infoboxes = pd.read_html(url, index_col=0, attrs={"class": "infobox"})
            infobox = infoboxes[0]
            address_info = infobox.loc["Headquarters"].values[0]
            return address_info


def donate():
    wikipedia.donate()

def change_language():
    wikipedia.languages()
    lang = input("Which language would you like the fetched articles to be in? (Ex. EN/SP/HE) ")
    wikipedia.set_lang(lang)

# def get_lapd_address():
#   page = wikipedia.WikipediaPage("Los Angeles Police Department")
#   page_content = page.content
#   content_list = page_content.split()
#   for index, word in enumerate(content_list):
#       if word == 'headquartered':
#           return " ".join(content_list[index + 2: index + 11])


# def get_home_address():
#   page = wikipedia.WikipediaPage("Death of Marilyn Monroe")
#   page_content = page.content
#   content_list = page_content.split()
#   for index, word in enumerate(content_list):
#       if word == 'home' and content_list[index + 1] == 'at':
#               return " ".join(content_list[index + 2: index + 11])


# def get_agency_address():
#   page = wikipedia.WikipediaPage("William Morris Agency")
#   page_content = page.content
#   content_list = page_content.split()
#   studio_house_number = '202 '
#   for index, word in enumerate(content_list):
#       if word == 'Canon':
#           return studio_house_number + " ".join(content_list[index: index + 5])


# def get_studio_address():
#     url = 'https://en.wikipedia.org/wiki/20th_Century_Studios'
#     infoboxes = pd.read_html(url, index_col=0, attrs={"class": "infobox"})
#     infobox = infoboxes[0]
#     address_info = infobox.loc["Headquarters"].values[0]
#     return address_info
