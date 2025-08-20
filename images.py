import os
import pytesseract
from PIL import Image
import mysql.connector

# MariaDB connection
db = mysql.connector.connect(
    host="localhost",
    user="your_user",
    password="your_password",
    database="your_db"
)
cursor = db.cursor()

# Path to images
image_folder = "images"

# Loop through images
for filename in os.listdir(image_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        path = os.path.join(image_folder, filename)

        # OCR extraction
        text = pytesseract.image_to_string(Image.open(path))

        # Insert into MariaDB
        sql = "INSERT INTO ocr_results (filename, extracted_text) VALUES (%s, %s)"
        cursor.execute(sql, (filename, text))
        db.commit()

cursor.close()
db.close()
print("OCR completed and stored in DB.")
