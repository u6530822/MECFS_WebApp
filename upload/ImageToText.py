import pytesseract
from PIL import Image
import re
from pdf2image import convert_from_path
import xlsxwriter
import boto3
import DBAccessKey
import sys
import argparse

access_key_id_global = DBAccessKey.DBAccessKey.access_key_id_global
secret_access_key_global = DBAccessKey.DBAccessKey.secret_access_key_global

class ImageToText:

    def __init__(self, name):
        self.name = name

    def get_database_value():
        """
        Create an excel sheet with all the entries from the database
        Assumption: All fields have the same size
        """

        # Set up workbook and define its name
        workbook = xlsxwriter.Workbook('YourResults.xlsx')
        worksheet = workbook.add_worksheet()

        start = 0  # indicator to write either keys or values
        row = 0
        col = 2

        # Obtain values from the database
        database = boto3.resource('dynamodb', region_name='ap-southeast-2', aws_access_key_id=access_key_id_global,
                                  aws_secret_access_key=secret_access_key_global)
        table = database.Table('ME_CFS_DB')
        response = table.scan()

        for row_data in response['Items']:

            # Obtain keys and record them down in the first row of the sheet
            if start == 0:
                for (k, v) in row_data.items():
                    if k == "Reference_No":
                        worksheet.write(row, 0, k)  # write  at row 0, col 0
                    elif k == "Date_Time":
                        worksheet.write(row, 1, k)  # write  at row 0, col 1
                    else:
                        worksheet.write(row, col, k)  # write keys at row 0
                        col += 1
                start = 1
                row = 1
                col = 2

            # Obtain values and record them down in the following rows of the sheet
            for (k, v) in row_data.items():  # write values at other rows
                if k == "Reference_No":
                    worksheet.write(row, 0, str(v))
                elif k == "Date_Time":
                    worksheet.write(row, 1, str(v))  # write  at row 0, col 1
                else:
                    worksheet.write(row, col, str(v))
                    col += 1

            col = 2
            row += 1

        workbook.close()

    def extract_value(self, text_local, val_local, attribute):
        # text_local - Total Text paragraph in the form of a list. Each row is an element in the list.
        # val_local - row index
        # attribute - attribute to extract

        # modify character to cater for split in the selected line
        if 'Req. No.' in text_local[val_local] or 'Ref. Range' in text_local[val_local] \
                or 'Lab No.' in text_local[val_local] or 'Vitamin D' in text_local[val_local]:
            text_local[val_local] = text_local[val_local].replace('Req. No.', 'ReqNo')
            text_local[val_local] = text_local[val_local].replace('Ref. Range', 'RefRange')
            text_local[val_local] = text_local[val_local].replace('Lab No.', 'LabNo')
            text_local[val_local] = text_local[val_local].replace('Vitamin D', 'VitaminD')

        val_local1 = text_local[val_local].split()

        # Get index of the attribute, if present
        if attribute in val_local1:
            index = val_local1.index(attribute)
        else:
            index = -1

        # Avoid cases where there is no value after index
        if index != -1 and len(val_local1) > index + 1:
            # value after index is not actual value if the value starts with alphabet
            if val_local1[index + 1][0].isalpha():
                # Check next line for value by splitting next line
                val_local2 = text_local[val_local + 1].split()
                # Make sure line two has >= words as line one, make sure the index is numeric
                if index < len(val_local2) and val_local2[index][0].isnumeric():
                    return val_local2[index]
                # Case where symbol *,>,<
                elif index < len(val_local2) and (val_local2[index] == '*' or val_local2[index] == '>' or
                                                  val_local2[index] == '<') and \
                        (val_local2[index + 1][0].isnumeric()):
                    return val_local2[index + 1]
                else:
                    return "N/A"
            elif val_local1[index + 1] == '*' or val_local1[index + 1] == '>' or val_local1[index + 1] == '<':
                return val_local1[index + 2]
            else:
                return val_local1[index + 1]
        else:
            return "N/A"

    def print_filename(self):

        # list of dictionary
        file_dict = []
        filename = self.name.name
        file = self.name

        # if it is pdf
        if filename.lower().endswith('.pdf'):
            # Store all the pages of the PDF in a variable
            pages = convert_from_path(file, 300, thread_count=4, grayscale=True, transparent=True)

            # Counter to store images of each page of PDF to image
            image_counter = 1

            # Iterate through all the pages stored above
            for page in pages:
                # Declaring filename for each page of PDF as png
                filename = filename.replace(".pdf", "")
                filename_png = filename + "_" + str(image_counter) + ".png"
                # Save the image of the page in system
                page.save(filename_png, 'PNG')
                # Increment the counter to update filename
                image_counter = image_counter + 1
                # Convert image to text
                dictionary = ImageToText.ReturnObject(self, self.name)
                # Ignore empty pages (Since empty pages will always have the "filename" key,
                # len 1 is treated as empty page)
                if len(dictionary) != 1:
                    file_dict.append(dictionary)

        else:
            dictionary = ImageToText.ReturnObject(self, self.name)
            # Ignore empty pages (Since empty pages will always have the "filename" key,
            # len 1 is treated as empty page)
            if len(dictionary) != 1:
                file_dict.append(dictionary)

        # return list of dictionary
        return file_dict


    def ReturnObject(self,filename):

        image = Image.open(filename)
        # Configure tesseract to treat each document line as a single line by setting --psm to 6
        text = pytesseract.image_to_string(image, lang="eng", config='--psm 6').splitlines()

        global Ref_no
        global Collected_Date_time

        result_dict = {
            "File_name": filename.name
        }

        # TODO: Improve logic of looping to reduce processing time
        for val in range(len(text)):
            if 'Collected' in text[val]:
                # remove alphabets
                Collected_Date_time = ''.join(i for i in text[val] if i.isdigit())
                Collected_Date_time = Collected_Date_time.replace("/", '')
                Collected_Date_time = Collected_Date_time.replace(" ", '')
                Collected_Date_time = Collected_Date_time.replace(":", '')
                result_dict['Date_Time'] = Collected_Date_time

            elif 'Reference:' in text[val]:
                Ref_no = ImageToText.extract_value(self, text, val, 'Reference:')
                if Ref_no == "N/A" and 'Reference_No' not in result_dict:
                    result_dict['Reference_No'] = "N/A"
                elif Ref_no != "N/A":
                    result_dict['Reference_No'] = Ref_no

            # Spaces surrounding PTH are to ensure other variation of PTH is not taken into account. Eg: PTH-C
            elif ' PTH ' in text[val]:
                pth = ImageToText.extract_value(self, text, val, 'PTH')
                if pth == "N/A" and 'Parathyroid_Hormone' not in result_dict:
                    result_dict['Parathyroid_Hormone'] = "N/A"
                elif pth != "N/A":
                    result_dict['Parathyroid_Hormone'] = pth

            elif 'Vitamin D' in text[val]:
                vitamin_d = ImageToText.extract_value(self, text, val, 'VitaminD')
                if vitamin_d == "N/A" and 'Vitamin_D' not in result_dict:
                    result_dict['Vitamin_D'] = "N/A"
                elif vitamin_d != "N/A":
                    result_dict['Vitamin_D'] = vitamin_d

            elif text[val]:
                field_str_list = ['Sodium', 'Potassium', 'Chloride', 'Bicarbonate', 'Urea', 'Creatinine', 'eGFR',
                                  'T.Protein', 'Albumin', 'ALP', 'Bilirubin', 'GGT',
                                  'AST', 'ALT', 'HAEMOGLOBIN', 'RBC', 'PCV', 'MCV', 'MCHC', 'RDW', 'wcc', 'Neutrophils',
                                  'Lymphocytes', 'Monocytes',
                                  'Eosinophils', 'Basophils', 'PLATELETS', 'ESR']

                for field_str in field_str_list:
                    if text[val].startswith(field_str):
                        result_str = ImageToText.extract_value(self, text, val, field_str)
                        if result_str == "N/A" and field_str not in result_dict:
                            result_dict[field_str] = "N/A"
                        elif result_str != "N/A":
                            result_dict[field_str] = result_str

                if text[val].startswith('MCH') and not text[val].startswith('MCHC'):
                    mch = ImageToText.extract_value(self, text, val, 'MCH')
                    if mch != "N/A":
                        result_dict['MCH'] = mch

        # return dictionary
        return result_dict

'''
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--a1', type=str)
    parser.add_argument('--a2', type=str)
    parser.add_argument('--a3', type=int)
    parser.add_argument('--a4', type=str)
    args = parser.parse_args()

    self = args.a1
    word_list = args.a2.split(',')  # ['1','2','3','4']
    index = args.a3
    word = args.a4

    #  python upload/ImageToText.py - -a1 = self - -a2 = "Vitamin D Vitamin,200,300" - -a3 = 0 - -a4 = VitaminD
    print(ImageToText.extract_value(self, word_list, index, word))
'''