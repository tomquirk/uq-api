"""
Catalogue scraper
"""
import re
import src.scrape.helpers as helpers
import src.settings as settings


def catalogue():
    """
    Scrapes list of programs identified by title and program code
    :return: List, of program codes
    """
    if settings.PROGRAMS_WHITELIST:
        return settings.PROGRAMS_WHITELIST

    program_list = []

    url = "https://future-students.uq.edu.au/study/find-a-program/listing/undergraduate"
    soup = helpers.get_soup(url)

    raw_programs = soup.find_all("a", href=re.compile("/study/program"))
    for raw_program in raw_programs:
        program_code = raw_program["href"][-4:]
        program_list.append(program_code)

    return program_list
