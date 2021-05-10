#  Copyright (c) 6/5/20, 1:41 AM.
#  Author 'Virgil Hoover'
#  License 'MIT License'

from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_water_mark(input_file: str, watermark: str) -> bool:
    """ Watermark a PDF and password protects it """
    # Check to ensure files are PDFs before proceeding
    try:
        if (input_file.endswith('.pdf')) or (watermark.endswith('.pdf')):
            output_file = 'watermark.pdf'
            watermark_obj = PdfFileReader(watermark)
            watermark_page = watermark_obj.getPage(0)
            pdf_reader = PdfFileReader(input_file)
            pdf_writer = PdfFileWriter()
            for page in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page)
                page.mergePage(watermark_page)
                pdf_writer.addPage(page)
            if input('Do you want to encrypt? (y/n) ').lower() == 'y':
                owner_password = input('Enter the owner password to be used: ')
                if input('The default user password is "letmein" do you want to use it? (y/n) ').lower() == 'y':
                    user_password = 'letmein'
                else:
                    user_password = input('Enter the user password to be used: ')
                pdf_writer.encrypt(user_pwd=user_password, owner_pwd=owner_password, use_128bit=True)
            with open(output_file, 'wb') as output:
                pdf_writer.write(output)
            return True
        else:
            print('Files have to be strings i.e. c:/some/path/some_file.pdf',
                  '\n*Note files must be PDFs or this function will error*')
            return False
    except FileNotFoundError:
        print('Files were not found!')
        return False
    except IOError:
        print('Files not accessible, please verify accessibility.')
        return False


if __name__ == '__main__':
    path = input('Please enter the path: ')
    file_input = path + 'FlowChart.pdf'
    watermark_file = path + 'WaterMark.pdf'
    if pdf_water_mark(file_input, watermark_file):
        print('File has been watermarked and is in the', path, 'directory.')
