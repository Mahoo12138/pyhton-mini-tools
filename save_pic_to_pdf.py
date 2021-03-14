import requests
import fitz
import glob

# 爬取图片
def CollectIMG(book_path,book_pages):
    for page in range(1,262):
        with open(r"D:\Code\PythonProjects\pyhton-mini-tools\pic\\" + str(page) + '.jpg','wb') as img:
            img.write(requests.get("https://book.yunzhan365.com/kbms/ykjg/files/mobile/" + str(page) + ".jpg").content)
            print("第{0!s}张图片保存成功！".format(page))

# 转换 pdf

def ConvertPDF(img_path, pdf_path, pdf_name):
    print("正在转换为PDF中")
    doc = fitz.open()
    for img in sorted(glob.glob(img_path + "\*.jpg")):
        imgdoc = fitz.open(img)
        pdfbytes = imgdoc.convertToPDF()
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)
    doc.save(pdf_path + pdf_name)
    doc.close()

if __name__ == '__main__':
    ConvertPDF(r"D:\Code\PythonProjects\pyhton-mini-tools\pic\\",r"D:\Code\PythonProjects\pyhton-mini-tools\pic\\","信号与系统.pdf")