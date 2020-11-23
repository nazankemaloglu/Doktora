from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
import io
import nltk
nltk.download('punkt')

def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)
            
            text = fake_file_handle.getvalue()
            yield text
    
            # close open handles
            converter.close()
            fake_file_handle.close()
    
def extract_text(pdf_path):
    tot = {}
    for i, page in enumerate(extract_text_by_page(pdf_path)):
        tot.update({i+1 : page})
    return tot

if __name__ == "__main__":
    path = "/home/linux/İndirilenler/Tez-main/2.pdf"
    pdf_miner = extract_text(path)
    print('The pdf has {} pages and the data structure is a {} where the index refers to the page number.'.format( ((list(pdf_miner.keys())[0])) , type(pdf_miner)))

text=[]
for key,val in pdf_miner.items():
    text.append(val)
s=(" ".join(text))
s = s.replace('vb.', 'vb')
s = s.replace('vd.', 'vd')
s = s.replace('?', '')
s = s.replace('Eş.', 'Eş')

a_list = nltk.tokenize.sent_tokenize(s)

abstract = [i for i, x in enumerate(a_list) if 'Keywords' in x]

indis=abstract[0]+1
a_list=a_list[indis:]
indices = [i for i, x in enumerate(a_list) if 'KAYNAK' in x]
i=indices[0]
a_list=a_list[:i]

for el in a_list:
    if len(el)<12:
        a_list.remove(el)
        
[x for x in a_list if "[" in x ]

'''
#d=list(filter(None, s.split('  ')))
text_file = open("Output.txt", "w")
text_file.write("Purchase Amount: %s" % s)
text_file.close()
'''

