# Import modules
import os

PROJECT_PATH = "/Users/lisa/VSCodeProjects/GuessWho/"

BLANK_NAME = "blank.jpg"
BLANK_PATH = PROJECT_PATH + "API/" + BLANK_NAME
PATH_DESTINATION = PROJECT_PATH + "IMAGE_OUTPUT/"

for i in range(25):

    os.system('cp ' + BLANK_PATH + " " + PATH_DESTINATION + str(i // 5 + 1) + "x" + str(i % 5 + 1) + ".jpg")