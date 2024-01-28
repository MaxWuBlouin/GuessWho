# Import modules
import requests
import json
import os

# Redefine this after download
PROJECT_PATH = "/Users/lisa/VSCodeProjects/GuessWho/"

#Directory names
START_DIRECTORY = PROJECT_PATH + "IMAGE_INPUT/"
UPLOAD_DIRECTORY = "/Faces/"
URL_PATH = "https://maxwublouin.sirv.com/Faces/"
DESTINATION_PATH = "IMAGE_OUTPUT/"

# URL extension names
SQUARE_RATIO = "crop.aspectratio=1:1"
SCALE_SIZE = "ch=300"
CROP_FACE = "crop.type=face"
FACE_INDEX = "crop.face="

# Total number of pictures used
picCount = [0]

# Get token
def getToken():
    url = 'https://api.sirv.com/v2/token'

    payload = {
      'clientId': 'Za363g1RB7ATSj6dGzy4Z0Jz5iV',
      'clientSecret': 'xrPg4gT+9/dEEj/Tqm1wnX+IQvplSvxRkSPwvYQvF7RfbO2L7ltvZ23RT4f4MKaMhBV09HT7p7ZTeFPsK+1VNA=='
    }

    headers = {'content-type': 'application/json'}

    response = requests.request('POST', url, data=json.dumps(payload), headers=headers)

    token = response.json()['token']

    return token
        
# Upload an image to API given path name
def uploadImagePath(startPath, targetPath):
    
    url = 'https://api.sirv.com/v2/files/upload'
    
    querystring = {"filename": targetPath}
    
    payload = open(startPath, "rb")

    headers = {
      'content-type': 'image/jpeg',
      'authorization': 'Bearer %s' % token
    }

    response = requests.request('POST', url, data=payload, headers=headers, params=querystring)

# Upload an image to API given image name
def uploadImage(imageName):
    
    startPath = START_DIRECTORY + imageName
    targetPath = UPLOAD_DIRECTORY + imageName

    uploadImagePath(startPath, targetPath)

# Download an image from URL
def downloadImage(imageURL, targetRelativePath):
    with open(targetRelativePath, "wb") as handle:
        response = requests.get(imageURL, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break
            
            handle.write(block)

# Return number of faces on image URL
def howManyFaces(imageName):
    
    downloadImage(URL_PATH + imageName + "?crop.type=face", DESTINATION_PATH + "test.jpg")

    os.remove(PROJECT_PATH + DESTINATION_PATH + "test.jpg")

    jsonURLpath = URL_PATH + imageName + "?info"

    downloadImage(jsonURLpath, DESTINATION_PATH + "info.json")
    
    f = open(PROJECT_PATH + DESTINATION_PATH + "info.json")

    data = json.load(f)

    numFacesDetected = len(data["original"]["smartcrop"]["faces"]["faces"])

    f.close()

    os.remove(PROJECT_PATH + DESTINATION_PATH + "info.json")

    return numFacesDetected

# Download face given image URL and index
def getFace(imageURL, targetRelativePath, index):
    
    newImageURL = imageURL + "?" + CROP_FACE + "&" + FACE_INDEX + str(index) + "&" + SQUARE_RATIO + "&" + SCALE_SIZE + "&" + "&crop.confidence=0.3"
    print(newImageURL)

    downloadImage(newImageURL, targetRelativePath)

# Download specified number of faces from image URL
def getAllFaces(imageName, targetRelativeDirectory):
    
    imageURL = URL_PATH + imageName

    numImages = howManyFaces(imageName)
    
    for i in range(numImages):
        
        targetRelativePath = targetRelativeDirectory + str(picCount[0] // 5 + 1) + "x" + str(picCount[0] % 5 + 1) +".jpg"

        getFace(imageURL, targetRelativePath, i)

        picCount[0] += 1

# Given image, return faces
def uploadAndGet(imageName):
    
    uploadImage(imageName)

    getAllFaces(imageName, DESTINATION_PATH)


# Test functions
token = getToken()

for image in os.listdir(START_DIRECTORY):
    
    uploadAndGet(image)
