from PyPDF2 import PdfFileReader, PdfFileWriter

def Crop():
    file = PdfFileReader('C:/Users/sgkha/PycharmProjects/untitled2/file.pdf','r')
    file_1= PdfFileWriter()

    page = file.getPage(1)
    U_L =page.cropBox.getUpperLeft() # 21.5

    for i in range(file.numPages):
        n = int(input("How many cm to crop ?"))
        page = file.getPage(i)
        page.cropBox.setUpperLeft((0,U_L[1]))
        page.cropBox.setLowerLeft((0,n*28))
        file_1.addPage(page)

    new_file = open('NEW.pdf', 'wb')
    file_1.write(new_file)

    return new_file.close()


a = Crop()

