import re


def clean_text(text):
    """
    Performs light text cleaning while preserving meaning.
    """
    text = text.lower() #Lowercase removes case mismatch
    text = text.strip() #removes extra spaces
    text = re.sub(r"[^a-z0-9\s]", "", text) #Keeps letters and numbers,Removes punctuation like ? , ! ‘ ’
    text = re.sub(r"\s+", " ", text) #Remove Extra Spaces
    return text
