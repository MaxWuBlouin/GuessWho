# Import modules
import os

def cleanup():

    PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))[:-3]
    
    BLANK_NAME = "blank.jpg"
    BLANK_PATH = PROJECT_PATH + "API/" + BLANK_NAME
    PATH_DESTINATION = PROJECT_PATH + "HTML_SITE/IMAGE_OUTPUT/"

    BAD_DS = ".DS_Store"

    if os.name == 'nt':  # Windows
        os_cmd = 'copy '
    else:  # Unix/Linux
        os_cmd = 'cp '

    try:
        os.remove(PROJECT_PATH + BAD_DS)
    except OSError:
        pass

    try:
        os.remove(PROJECT_PATH + "API/" + BAD_DS)
    except OSError:
        pass

    try:
        os.remove(PROJECT_PATH + "HTML_SITE/" + BAD_DS)
    except OSError:
        pass

    try:
        os.remove(PROJECT_PATH + "HTML_SITE/" + "IMAGE_OUTPUT/" + BAD_DS)
    except OSError:
        pass

    try:
        os.remove(PROJECT_PATH + "IMAGE_INPUT/" + BAD_DS)
    except OSError:
        pass

    for i in range(25):

        os.system(os_cmd + BLANK_PATH + " " + PATH_DESTINATION + str(i // 5 + 1) + "x" + str(i % 5 + 1) + ".jpg")