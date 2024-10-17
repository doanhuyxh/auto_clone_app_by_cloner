import os
import time
from termcolor import colored

import libs.ld_script as ld
import libs.open_cv as cv
import libs.tesseract as tess

from libs.clear_cache import clear_all_pycache

clear_all_pycache()


def GetScreenShot(nameLD):
    ld.takeScreen(nameLD)
    ld.getScreen(nameLD)
    temp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "libs", "temp")
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    return os.path.join(temp_dir, f"{nameLD}.png")


def Click_Text(nameLD, text, time_check=3):
    for i in range(time_check):
        try:
            print(colored(f"click {text} : {i}", "light_green"))
            image_path = GetScreenShot(nameLD)
            pos = tess.get_text_positions(text, image_path)
            os.remove(image_path)
            if pos is not None:
                x, y = pos
                ld.click(nameLD, x, y)
                break
            else:
                print(colored(f"finding {text} : {i}", "yellow"))
                time.sleep(2)
                if i == time_check - 1:
                    return False
        except Exception as e:
            print(colored(f"finding {text} : {i}", "yellow"))
            time.sleep(2)
            if i == time_check - 1:
                return False

    return True


def Click_Paragraph(nameLD, paragraph, time_check=3):
    for i in range(time_check):
        image_path = GetScreenShot(nameLD)
        pos = tess.get_paragraph_positions(paragraph, image_path)
        os.remove(image_path)
        if pos is not None:
            x, y = pos
            ld.click(nameLD, x, y)
            break
        else:
            print(colored(f"finding {paragraph} : {i}", "yellow"))
            time.sleep(2)
            if i == time_check - 1:
                return False
    return True


def Click_Images(nameLd, template, timeCheck=3):
    for i in range(timeCheck):
        try:
            image_path = GetScreenShot(nameLd)
            pos = cv.find_template_in_image(template, image_path)
            os.remove(image_path)
            if pos is not None:
                x, y = pos
                ld.click(nameLD, x, y)
                break
            else:
                print(colored(f"finding {template} : {i}", "yellow"))
                time.sleep(2)
                if i == timeCheck - 1:
                    return False
        except Exception as e:
            print(colored(f"finding {template} : {i}", "yellow"))
            time.sleep(2)
            if i == timeCheck - 1:
                return False
    return True


def CloneApp(nameLD, phone, NumberClone):

    ld.pressKey(nameLD, "KEYCODE_HOME")

    Click_Text(nameLD, "Cloner")
    time.sleep(5)
    Click_Text(nameLD, "Telegram")

    if NumberClone > 1:
        Click_Images(
            nameLD,
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "images", "so_nhan_ban.png"
            ),
        )

        Click_Images(
            nameLD,
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "images", "plus.png"
            ),
        )

        Click_Images(
            nameLD,
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "images", "ok.png"
            ),
        )

    Click_Images(
        nameLD,
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "images", "edit_name.png"
        ),
    )

    time.sleep(2)
    ld.sendText(nameLD, phone)

    Click_Images(
        nameLD,
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "ok.png"),
    )

    Click_Images(
        nameLD,
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "tick.png"),
    )

    Click_Paragraph(nameLD, "CHO PHEP")

    Click_Text(nameLD, "OK")

    Click_Images(
        nameLD,
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "images", "cai_dat_ung_dung.png"
        ),
        50,
    )

    Click_Images(
        nameLD,
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "images", "cai_dat.png"
        ),
        50,
    )

    check = Click_Images(
        nameLD,
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "images", "khoi_chay.png"
        ),
        50,
    )

    if check:
        print(colored("Clone success", "green"))
    else:
        print(colored("Clone failed", "red"))

    return check


nameLD = "Telegram"

# ld.copyLD(nameLD, "goc")
# ld.modLD(nameLD)
# ld.runLD(nameLD)
# time.sleep(10)

with open("./phone.txt", "r") as f:
    phones = f.readlines()
    NumberClone = 1
    for phone in phones:
        phone = phone.strip()
        if NumberClone == 9:
            with open("./check_point.txt", "w") as f:
                f.write("".join(phones[NumberClone:]))
            break
        print(colored(f"Cloning {phone}", "blue"))
        CloneApp(nameLD, phone, NumberClone)
        NumberClone += 1
        time.sleep(5)
