import os
import time
import libs.ld_script as ld
import libs.open_cv as cv
import libs.tesseract as tess

nameLD= "goc"

ld.pressKey(nameLD, "KEYCODE_HOME")
ld.takeScreen(nameLD)
ld.getScreen(nameLD)
image_path = os.path.dirname(os.path.abspath(__file__))+"\\libs\\temp\\"+nameLD+".png"
print(tess.ocr_image("./temp/"+nameLD+".png"))
pos = tess.get_text_positions("OK", "./temp/"+nameLD+".png")
print(pos)
x,y = pos
ld.click(nameLD, x,y)

#ld.pressKey(nameLD, "KEYCODE_DEL")

#ld.sendText(nameLD, "84523395871")
#template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "cai_dat_ung_dung.png")
#pos= cv.find_template_in_image(f"{template_path}", image_path)
#print(pos)
# x,y = pos
# ld.click(nameLD, x, y)
