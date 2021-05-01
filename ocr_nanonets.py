from nanonets import ImageClassification
import os
from nanonets import OCR


api_key='3wrvv2Weyy5f1XgOCZN4zu7hwCBYfzM3'
categories=['Name','RosterDay','RosterStartDate','RosterType']
model_id1="e06c2cf5-dd83-4500-bf8d-46c9bdd2aab5"


model = OCR(api_key, categories, model_id=model_id1)
img_dir=("C:\\Users\\Crover\\source\\repos\\PersonalRepos\\python_stuffs\\ptest_images_nanonets")
imglist = os.listdir(img_dir)
imglist = [img_dir + '\\' + x for x in imglist]
img_loc = ('C:\\Users\\Crover\\source\\repos\\PersonalRepos\\python_stuffs\\ptest_images_nanonets\\ptest1.jpg')

## prediction functions for single file
resp_one_file = model.predict_for_files(imglist)
print("IC response - single image: ", resp_one_file)


# import requests

# url = 'https://app.nanonets.com/api/v2/OCR/Model/e06c2cf5-dd83-4500-bf8d-46c9bdd2aab5/LabelFile/'

# data = {'file': open('page_1.jpg', 'rb')}

# response = requests.post(url, auth=requests.auth.HTTPBasicAuth('3wrvv2Weyy5f1XgOCZN4zu7hwCBYfzM3', ''), files=data)

# print(response.text)

# # Creating a text file to write the output
# outfile = "out_text_nanonets.txt"
  
# # Open the file in append mode so that 
# # All contents of all images are added to the same file
# f = open(outfile, "a")
# f.write(response.text)

# f.close