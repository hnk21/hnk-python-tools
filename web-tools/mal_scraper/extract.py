import re
from datetime import datetime

def get_sidebar_value(soup, label):
    element = soup.find('span', string=label)
    
    if element:
        clean_text = element.parent.text.replace(label, '').strip()
        return re.sub(r'\s+', ' ', clean_text)
    
    return "N/A"

def get_start_date(text):
    if not text or text == "N/A" or text == "Unknown": return None
    start_date_str = text.split(' to ')[0].strip()
    formats = ['%b %d, %Y', '%b %Y', '%Y']

    for fmt in formats:
        try:
            dt = datetime.strptime(start_date_str, fmt)
            return dt.strftime('%Y-%m-%d')
        except ValueError:
            continue
    
    return start_date_str

def get_anime_details(soup):
    title_jp    = get_sidebar_value(soup, 'Japanese:')
    episodes    = get_sidebar_value(soup, 'Episodes:')
    airing_date = get_sidebar_value(soup, 'Aired:')
    airing_start_date = get_start_date(airing_date)

    return [title_jp, episodes, airing_start_date]