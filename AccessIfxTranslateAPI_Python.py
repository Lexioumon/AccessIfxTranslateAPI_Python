import requests
import docx2txt

url = "https://translate.infineon.com/api/deepl/v2/translate?auth_key=vm6HY80haOwpjSx9xani1GrN39bcNkdaNkBD38DTOSMATcsdvrTicSDPaRmsA7f5xDVxYIFxaBcvy2f35Lqe4qEjU4OfqZZtwG4S"

infile = r"C:\Users\LiuXiaome\Documents\WorkSpace\Project\TranslateDocs_UsingAI\infineonMT\input\testfile.txt"
outfile = r"C:\Users\LiuXiaome\Documents\WorkSpace\Project\TranslateDocs_UsingAI\infineonMT\output\testresult.txt"

with open(infile, 'r') as ifl:
    text = ifl.read()

data = {
        "auth_key": "vm6HY80haOwpjSx9xani1GrN39bcNkdaNkBD38DTOSMATcsdvrTicSDPaRmsA7f5xDVxYIFxaBcvy2f35Lqe4qEjU4OfqZZtwG4S",
        "text": text,
        "source_lang": "EN",
        "target_lang": "ZH",
        "split_sentences": "nonewlines",
        "preserve_formatting": "1"
        }

headers = {
    "accept": "application/json",
    'Content-Type': 'application/x-www-form-urlencoded'
    }

response = requests.post(url, data=data, headers=headers,verify=False)

with open(outfile, "w", encoding="utf-8") as ofl:
    ofl.write(response.json()["translations"][0]["text"])