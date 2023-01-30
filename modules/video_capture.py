import cv2
import os
import pprint
import dotenv
from pathlib import Path

##############################################
### LOAD ENV AND INITIALIZE PRETTY PRINTER ###
##############################################

dotenv.load_dotenv()
pp = pprint.PrettyPrinter(indent=2).pprint

dataset_path = os.getenv('RAW_SECTION_A')
print(dataset_path)
#
# # pp(dataset_path)
# cap = cv2.VideoCapture(dataset_path + '\\sub01\\EP01_5\\EPO1_5-1%02d.jpg')
#
# while True:
#     ret, frame = cap.read()
#     if ret:
#         cv2.imshow('Frame', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
#
# cap.release()
# cv2.destroyAllWindows()