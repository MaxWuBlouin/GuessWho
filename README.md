# GuessWho
Note: this program currently does not work on Windows.

Instructions:
- First, copy some images of people into the folder named IMAGE_INPUT. There should be a maximum of 25 faces in all the images.
- Run FaceAPI.py. This will generate cropped images of each faces from the images in IMAGE_INPUT. Wait until the program finishes running (it should print "done!" to the terminal)
- Open index.html (in the HTML_SITE directory) in a web browser.
- Enjoy! You can click on the images to toggle back and forth between showing and hiding them.

Troubleshooting:
- If certain images aren't loading on your browser, that means your probably opened/refreshed index.html while a python script was running. Wait for the python script to finish running, then refresh the page again.
- If you receive an error message in your terminal while running FaceAPI.py, the API likely couldn't find a face on one of your images. Try running the program again, but without that image.
