import os

Input = "/Users/skumara/Desktop/Sanjeev_Work/Hack_day_2019/Badads/Creative_Screnshots"
Output = "/Users/skumara/Desktop/Sanjeev_Work/Hack_day_2019/Badads/Extracted_text_files"

count = 0

for files in os.listdir(Input):
	count = count + 1
	cmd = ("tesseract " + Input + "/" + files + " " + Output + "/" + files + " " + "hocr")
	os.system(cmd)
	print count




from bs4 import BeautifulSoup

file = "/Users/skumara/Desktop/Sanjeev_Work/Hack_day_2019/Badads/Badkeyword.txt"

count = 0

abc = "/Users/skumara/Desktop/Sanjeev_Work/Hack_day_2019/Badads/Extracted_text_files/four.png.hocr"
soup = BeautifulSoup(open(abc), "html.parser")    
for city in soup.find_all('span', {'class' : 'ocrx_word'}):
    count = count + 1
    final = city.text
    #print final
    
    with open(file) as f:
        for line in f:
            domain = line.strip('\n')
           # print domain
            if (final == domain):
                print "Match"
                print final
            else:
                #print "Doesn't Match"
                print ""