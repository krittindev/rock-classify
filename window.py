import tkinter as tk
from tkinter import Tk
from PIL import Image, ImageTk
from tkinter.ttk import Frame, Label, Button, Style, Separator
import webbrowser

FLOWCHART_URL = 'https://60bb44df-a-62cb3a1a-s-sites.googlegroups.com/site/bhxsci58/hnwy-kar-reiyn-ru/4-thrni-prawati/Slide2.JPG'
ROCK_URL = 'https://raw.githubusercontent.com/tuliptgr/rock-classify/main/'
CLASSIFIER = {}


def setData():
    global CLASSIFIER
    CLASSIFIER = {
        "question": "เนื้อหิน",
        "choices": {
            "เม็ดกรวด": {
                "answer": "หินกรวดมน",
                "url": "./asset/rocks/conglomerate.jpg"
            },
            "ละเอียด": {
                "question": "รอยขนานเป็นชั้น",
                "choices": {
                    "ใช่": {
                        "question": "เนื้อแน่น",
                        "choices": {
                            "ใช่": {
                                "answer": "หินชนวน",
                                "url": "./asset/rocks/slate.jpg"
                            },
                            "ไม่ใช่": {
                                "answer": "หินดินดาน",
                                "url": "./asset/rocks/shale.jpg"
                            }
                        }
                    },
                    "ไม่ใช่": {
                        "question": "ทำปฏิกิริยากับกรด",
                        "choices": {
                            "ใช่": {
                                "answer": "หินปูน",
                                "url": "./asset/rocks/limestone.jpg"
                            },
                            "ไม่ใช่": {
                                "question": "ตรวจสี",
                                "choices": {
                                    "สีเทาอ่อน มีรูพรุน": {
                                        "answer": "หินพัมมิซ",
                                        "url": "./asset/rocks/pumice.jpg"
                                    },
                                    "สีเทา": {
                                        "answer": "หินบะซอลต์",
                                        "url": "./asset/rocks/basalt.jpg"
                                    },
                                    "สีเทาดำ": {
                                        "answer": "หินไดออไรต์",
                                        "url": "./asset/rocks/rhyolite.jpg"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "หยาบ": {
                "question": "การประสานของเนื้อหิน",
                "choices": {
                    "แข็งแรง": {
                        "question": "ริ้วหยัก",
                        "choices": {
                            "ใช่": {
                                "answer": "หินไนซ์",
                                "url": "./asset/rocks/gneiss.jpg"
                            },
                            "ไม่ใช่": {
                                "question": "ผลึกแร่ 3 ชนิด",
                                "choices": {
                                    "ใช่": {
                                        "answer": "หินแกรนิต",
                                        "url": "./asset/rocks/granite.jpg"
                                    },
                                    "ไม่ใช่": {
                                        "question": "ทำปฏิกิริยากับกรด",
                                        "choices": {
                                            "ใช่": {
                                                "answer": "หินอ่อน",
                                                "url": "./asset/rocks/marble.jpg"
                                            },
                                            "ไม่ใช่": {
                                                "answer": "หินควอร์ตไซต์",
                                                "url": "./asset/rocks/quartzite.jpg"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "ไม่แข็งแรง": {
                        "answer": "หินทราย",
                        "url": "./asset/rocks/sandstone.jpg"
                    }
                }
            }
        }
    }


root = Tk()

# Styles
FONT_FAMILY = "TH SarabunPSK"
FONT_SIZE_HEADER = 36
FONT_SIZE_BODY = 20
FONT_SIZE_BODY_AUTHOR = 15
Style(root).configure("header.TLabel", font=(
    FONT_FAMILY, FONT_SIZE_HEADER, "bold"))
Style(root).configure("body.TLabel", font=(
    FONT_FAMILY, FONT_SIZE_BODY, "bold"))
Style(root).configure("bodyAuthor.TLabel", font=(
    FONT_FAMILY, FONT_SIZE_BODY_AUTHOR, "bold"))
Style(root).configure("TButton", font=(FONT_FAMILY, FONT_SIZE_BODY, "bold"))

# Pages
WIDTH_FRAME = 720
HEIGHT_FRAME = 480
PADDING_FRAME = 50
homePage = Frame(root, width=WIDTH_FRAME,
                 height=HEIGHT_FRAME, padding=PADDING_FRAME)
formPage = Frame(root, width=WIDTH_FRAME,
                 height=HEIGHT_FRAME, padding=0)
authorPage = Frame(root, width=WIDTH_FRAME,
                   height=HEIGHT_FRAME, padding=0)
flowchartPage = Frame(root, width=1920,
                      height=1080, padding=5)
homePage.pack_propagate(False)
formPage.pack_propagate(False)
authorPage.pack_propagate(False)
flowchartPage.pack_propagate(False)

# Images
author1Image = ImageTk.PhotoImage(Image.open("./asset/author_1.jpg"))
author2Image = ImageTk.PhotoImage(Image.open("./asset/author_2.png"))
flowChartImage = ImageTk.PhotoImage(Image.open("./asset/flowchart.jpg"))
    

# Recursion B: Display Choice with Dictionary of Choices and Cut Out Unused Part of Dictionary
# Note: I use recursion in this part to prevent the overlap of temporary variable.


def createChoices(homePage, formPage, choisesDict):
    if len(choisesDict) > 0:
        choice = next(iter(choisesDict))
        subDictData = choisesDict[choice]
        choisesDict.pop(choice)
        Button(formPage, text=choice, style="TButton", command=lambda: classifierForm(homePage, formPage, subDictData)).pack(
            side=tk.TOP, expand=True)
        createChoices(homePage, formPage, choisesDict)

# Recursion A: Display Form Window with Dictionary of Data and call Nest Recursion for Create Choices


def classifierForm(homePage, formPage, dictData):
    for widget in formPage.winfo_children():
       widget.destroy()
    formPage.pack_forget()
    if "question" in dictData:
        Label(formPage, text=dictData["question"], style="header.TLabel").pack(
            side=tk.TOP, expand=True, pady=(50,20))
        createChoices(homePage, formPage, dictData["choices"])
        Button(formPage, text="ออก", style="TButton",
            command=lambda: changePage(formPage, homePage)).pack(side=tk.BOTTOM, expand=False, pady=(0,50))
        Separator(formPage, orient="horizontal").pack(
            side=tk.BOTTOM, fill=tk.X, padx=50, pady=(0,20))
    else:
        stoneImage = ImageTk.PhotoImage(Image.open(dictData["url"]).resize((720,480), Image.ANTIALIAS))
        stoneLabel = Label(formPage, image=stoneImage)
        stoneLabel.image = stoneImage
        stoneLabel.place(x=0,y=0)
        Button(formPage, text="ออก", style="TButton",
            command=lambda: changePage(formPage, homePage)).pack(side=tk.BOTTOM, expand=False, pady=20)
    formPage.pack()
            
def changePage(firstPage, secondPage):
    firstPage.pack_forget()
    secondPage.pack()

def startForm(homePage, formPage):
    setData()
    classifierForm(homePage, formPage, CLASSIFIER)
    changePage(homePage, formPage)


# widgets of Home Page
Label(homePage, text="โปรแกรมจำแนกหิน", style="header.TLabel").pack(
    side=tk.TOP, expand=True)
Button(homePage, text="จำแนกหิน", style="TButton", command = lambda: startForm(
    homePage, formPage)).pack(side=tk.TOP, expand=True)
Button(homePage, text="ผู้จัดทำ", style="TButton", command=lambda: changePage(
    homePage, authorPage)).pack(side=tk.TOP, expand=True)
Button(homePage, text="ผังงาน", style="TButton", command=lambda: changePage(
    homePage, flowchartPage)).pack(side=tk.TOP, expand=True)
Button(homePage, text="ออก", style="TButton",
       command=root.destroy).pack(side=tk.TOP, expand=True)

# widgets of Author Page with grid
Label(authorPage, text="จัดทำโดย", style="header.TLabel").grid(
    row=0, column=0, columnspan=2, pady=PADDING_FRAME)
Label(authorPage, image=author1Image).grid(row=1, column=0)
Label(authorPage, image=author2Image).grid(row=1, column=1)
Label(authorPage, text="นายธนกร  แสงจันทร์",
      style="bodyAuthor.TLabel").grid(row=2, column=0)
Label(authorPage, text="นายสตินันต์ เเสงเเก้ว",
      style="bodyAuthor.TLabel").grid(row=2, column=1)
Label(authorPage, text="เลขที่ 9 ชั้นมัธยมศึกษาปีที่ 4/1 (โอเมก้า)",
      style="bodyAuthor.TLabel").grid(row=3, column=0, padx=20)
Label(authorPage, text="เลขที่ 12 ชั้นมัธยมศึกษาปีที่ 4/1 (โอเมก้า)",
      style="bodyAuthor.TLabel").grid(row=3, column=1, padx=20)
Button(authorPage, text="ออก", style="TButton", command=lambda: changePage(
    authorPage, homePage)).grid(row=5, column=0, columnspan=2, pady=PADDING_FRAME)

# widgets of Flowchart Page with grid
Label(flowchartPage, text="ผังงาน", style="header.TLabel").grid(
    row=0, column=0, columnspan=2)
Label(flowchartPage, image=flowChartImage).grid(row=1, column=0, columnspan=2)
Separator(flowchartPage, orient="horizontal").grid(
    row=3, column=0, columnspan=2)
Button(flowchartPage, text="ภาพเต็ม", style="TButton", command=lambda: webbrowser.open(
    FLOWCHART_URL)).grid(row=4, column=0)
Button(flowchartPage, text="ออก", style="TButton", command=lambda: changePage(
    flowchartPage, homePage)).grid(row=4, column=1)

# Start Program
homePage.pack()
root.geometry("720x480+400+150")
root.title("โปรแกรมจำแนกหิน")
root.mainloop()
