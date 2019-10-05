import pytesseract
from PIL import Image
import re
from pdf2image import convert_from_path


class ImageToText:

    def __init__(self, name):
        self.name = name

    def extract_value(self, text_local, val_local, attribute):
        # Total Text paragraph, text per line index, attribute to extract
        # extract whole text to string and number as different lines

        # modify character to cater for split
        if 'Req. No.' in text_local[val_local] or 'Ref. Range' in text_local[val_local] \
                or 'Lab No.' in text_local[val_local] or 'Vitamin D' in text_local[val_local]:
            text_local[val_local] = text_local[val_local].replace('Req. No.', 'ReqNo')
            text_local[val_local] = text_local[val_local].replace('Ref. Range', 'RefRange')
            text_local[val_local] = text_local[val_local].replace('Lab No.', 'LabNo')

            #  TODO: Change all string first before extract value out rather than changing one line at a time
            if re.search('Vitamin D(.*?)[\s]', (text_local[val_local])):
                text_local[val_local] = re.sub('Vitamin D(.*?)[\s]', 'VitaminD ', text_local[val_local])
            elif re.search('Vitamin D.*', (text_local[val_local])):
                text_local[val_local] = re.sub('Vitamin D.*', 'VitaminD', text_local[val_local])

        val_local1 = text_local[val_local].split()
        print(val_local1)

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
                print(val_local2)
                print(index)
                # Make sure line two has >= words as line one, make sure the index is numeric
                if index < len(val_local2) and val_local2[index][0].isnumeric():
                    return val_local2[index]
                # Case where symbol *,>,<
                elif index < len(val_local2) and (val_local2[index] == '*' or val_local2[index] == '>' or
                                                  val_local2[index] == '<') and \
                        (val_local2[index + 1][0].isnumeric()):
                    return val_local2[index + 1]
                else:
                    # print("N/A 1")
                    return "N/A"
            elif val_local1[index + 1] == '*' or val_local1[index + 1] == '>' or val_local1[index + 1] == '<':
                return val_local1[index + 2]
            else:
                return val_local1[index + 1]
        # check if next line has value
        elif index != -1 and len(text_local) > val_local + 1:
            # Check next line for value
            val_local2 = text_local[val_local + 1].split()
            # Make sure that value is in the same index in the next line and is numeric
            if len(val_local2) > index and val_local2[index][0].isnumeric():
                return val_local2[index]
            # Case where symbol *,>,<
            elif len(val_local2) > index and (val_local2[index] == '*' or val_local2[index] == '>'
                                              or val_local2[index] == '<') and (val_local2[index + 1][0].isnumeric()):
                return val_local2[index + 1]
            else:
                return "N/A"
        # if no next line or no index, return N/A
        else:
            return "N/A"

    def print_filename(self):

        # list of dictionary
        file_dict = []
        print(self.name)
        print("clear once")
        filename= self.name.name
        file= self.name

        print(type(filename))
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
                print("check")
                print(text[val])
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

        # return dictionary
        return result_dict



