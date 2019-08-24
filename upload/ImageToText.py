import pytesseract
from PIL import Image
import re

list_of_dict = []

class ImageToText:

    def __init__(self, name):
        self.name = name

    def extract_value(self, text_local, val_local, attribute):
        # extract whole text to string and number as different lines

        # modify character to cater for split
        if 'Req. No.' in text_local[val_local] or 'Ref. Range' in text_local[val_local] \
                or 'Lab No.' in text_local[val_local] or 'Vitamin D' in text_local[val_local]:
            text_local[val_local] = text_local[val_local].replace('Req. No.', 'ReqNo')
            text_local[val_local] = text_local[val_local].replace('Ref. Range', 'RefRange')
            text_local[val_local] = text_local[val_local].replace('Lab No.', 'LabNo')

            if re.search('Vitamin D(.*?)[\s]', (text_local[val_local])):
                text_local[val_local] = re.sub('Vitamin D(.*?)[\s]', 'VitaminD ', text_local[val_local])
            elif re.search('Vitamin D.*', (text_local[val_local])):
                text_local[val_local] = re.sub('Vitamin D.*', 'VitaminD', text_local[val_local])

        val_local1 = text_local[val_local].split()
        print(val_local1)
        index = val_local1.index(attribute)

        # Avoid cases where there is no value after index
        if len(val_local1) > index + 1:
            # value after index is not actual value if the value starts with alphabet
            if val_local1[index + 1][0].isalpha():
                # Check next line for value
                val_local2 = text_local[val_local + 1].split()
                if index < len(val_local2) and val_local2[index][0].isnumeric():
                    return val_local2[index]
                # Case where symbol *,>,<
                elif index < len(val_local2) and (
                        val_local2[index] == '*' or val_local2[index] == '>' or val_local2[index] == '<') \
                        and (val_local2[index + 1][0].isnumeric()):
                    return val_local2[index + 1]
                else:
                    return "N/A"
            elif val_local1[index + 1] == '*' or val_local1[index + 1] == '>' or val_local1[index + 1] == '<':
                return val_local1[index + 2]
            else:
                return val_local1[index + 1]
        else:
            # Check next line for value
            val_local2 = text_local[val_local + 1].split()
            if val_local2[index][0].isnumeric():
                return val_local2[index]
            # Case where symbol *,>,<
            elif (val_local2[index] == '*' or val_local2[index] == '>' or val_local2[index] == '<') \
                    and (val_local2[index + 1][0].isnumeric()):
                return val_local2[index + 1]
            else:
                return "N/A"



    def ReturnObject(self):

        image = Image.open(self.name)
        # Configure tesseract to treat each document line as a single line by setting --psm to 6
        text = pytesseract.image_to_string(image, lang="eng", config='--psm 6').splitlines()
        print("line 64 in returnobject")

        global Ref_no
        global Collected_Date_time

        result_dict = {
            "filename": self.name
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
                if pth == "N/A" and 'Parathyroid Hormone' not in result_dict:
                    result_dict['Parathyroid Hormone'] = "N/A"
                elif pth != "N/A":
                    result_dict['Parathyroid Hormone'] = pth

            elif 'Vitamin D' in text[val]:
                print("check")
                print(text[val])
                vitamin_d = ImageToText.extract_value(self, text, val, 'VitaminD')
                if vitamin_d == "N/A" and 'Vitamin D' not in result_dict:
                    result_dict['Vitamin D'] = "N/A"
                elif vitamin_d != "N/A":
                    result_dict['Vitamin D'] = vitamin_d

            elif text[val]:
                field_str_list = ['Sodium', 'Potassium', 'Chloride', 'Bicarbonate', 'Urea', 'Creatinine', 'eGFR',
                                  'T.Protein', 'Albumin', 'ALP', 'Bilirubin', 'GGT',
                                  'AST', 'ALT', 'HAEMOGLOBIN', 'RBC', 'PCV', 'MCV', 'MCHC', 'RDW', 'wcc', 'Neutrophils',
                                  'Lymphocytes', 'Monocytes',
                                  'Eosinophils', 'Basophils', 'PLATELETS', 'ESR']  # T.Protein

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

        list_of_dict.append(result_dict)
        return list_of_dict


