import tkinter as tk
from tkinter import Tk
from PIL import Image, ImageTk
from tkinter.ttk import Frame, Label, Button, Style, Separator
import webbrowser

FLOWCHART_URL = 'https://60bb44df-a-62cb3a1a-s-sites.googlegroups.com/site/bhxsci58/hnwy-kar-reiyn-ru/4-thrni-prawati/Slide2.JPG'
CLASSIFIER = {}


def setData():
    global CLASSIFIER
    CLASSIFIER = {
        "question": "เนื้อหิน",
        "choices": {
            "เม็ดกรวด": {
                "answer": "หินกรวดมน",
            },
            "ละเอียด": {
                "question": "รอยขนานเป็นชั้น",
                "choices": {
                    "ใช่": {
                        "question": "เนื้อแน่น",
                        "choices": {
                            "ใช่": {
                                "answer": "หินชนวน",
                            },
                            "ไม่ใช่": {
                                "answer": "หินดินดาน",
                            }
                        }
                    },
                    "ไม่ใช่": {
                        "question": "ทำปฏิกิริยากับกรด",
                        "choices": {
                            "ใช่": {
                                "answer": "หินชนวน",
                            },
                            "ไม่ใช่": {
                                "question": "ตรวจสี",
                                "choices": {
                                    "สีเทาอ่อน มีรูพรุน": {
                                        "answer": "หินพัมมิซ",
                                    },
                                    "สีเทา": {
                                        "answer": "หินบะซอลต์",
                                    },
                                    "สีเทาดำ": {
                                        "answer": "หินไดออไรต์",
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
                            },
                            "ไม่ใช่": {
                                "question": "ผลึกแร่ 3 ชนิด",
                                "choices": {
                                    "ใช่": {
                                        "answer": "หินแกรนิต",
                                    },
                                    "ไม่ใช่": {
                                        "question": "ทำปฏิกิริยากับกรด",
                                        "choices": {
                                            "ใช่": {
                                                "answer": "หินอ่อน",
                                            },
                                            "ไม่ใช่": {
                                                "answer": "หินควอร์ตไซต์",
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "ไม่แข็งแรง": {
                        "answer": "หินทราย",
                    }
                }
            },
        }
    }


root = Tk()

# Styles
FONT_FAMILY = "TH SarabunPSK"
FONT_SIZE_HEADER = 36
FONT_SIZE_BODY = 20
Style(root).configure("header.TLabel", font=(
    FONT_FAMILY, FONT_SIZE_HEADER, "bold"))
Style(root).configure("body.TLabel", font=(
    FONT_FAMILY, FONT_SIZE_BODY, "bold"))
Style(root).configure("TButton", font=(FONT_FAMILY, FONT_SIZE_BODY, "bold"))

# Pages
WIDTH_FRAME = 720
HEIGHT_FRAME = 480
PADDING_FRAME = 50
homePage = Frame(root, width=WIDTH_FRAME,
                 height=HEIGHT_FRAME, padding=PADDING_FRAME)
authorPage = Frame(root, width=WIDTH_FRAME,
                   height=HEIGHT_FRAME, padding=PADDING_FRAME)
homePage.pack_propagate(False)
authorPage.pack_propagate(False)

# Images
authorImage = ImageTk.PhotoImage(Image.open("./asset/author.jpg"))


def startForm():
    setData()
    classifierForm(CLASSIFIER)


def selectedChoice(window, dictData):
    window.destroy()
    classifierForm(dictData)


def createChoices(window, page, choisesDict):
    if(len(choisesDict) > 0):
        choice = next(iter(choisesDict))
        subDictData = choisesDict[choice]
        choisesDict.pop(choice)
        Button(page, text=choice, style="TButton", command=lambda: selectedChoice(window, subDictData)).pack(
            side=tk.TOP, expand=True)
        createChoices(window, page, choisesDict)


def classifierForm(dictData):
    window = Tk()
    Style(window).configure("header.TLabel", font=(
        FONT_FAMILY, FONT_SIZE_HEADER, "bold"))
    Style(window).configure("body.TLabel", font=(
        FONT_FAMILY, FONT_SIZE_BODY, "bold"))
    Style(window).configure("TButton", font=(
        FONT_FAMILY, FONT_SIZE_BODY, "bold"))
    page = Frame(window, width=WIDTH_FRAME,
                 height=HEIGHT_FRAME, padding=PADDING_FRAME)
    if(len(dictData) > 1):
        Label(page, text=dictData["question"], style="header.TLabel").pack(
            side=tk.TOP, expand=True)
        createChoices(window, page, dictData["choices"])
    else:
        Label(page, text=dictData["answer"], style="header.TLabel").pack(
            side=tk.TOP, expand=True)
    Button(page, text="ออก", style="TButton",
           command=window.destroy).pack(side=tk.BOTTOM, expand=False)
    Separator(page, orient="horizontal").pack(
        side=tk.BOTTOM, fill=tk.X, pady=20)
    page.pack_propagate(False)
    page.pack()
    window.geometry("720x480+400+150")
    window.mainloop()


def changePage(firstPage, secondPage):
    firstPage.pack_forget()
    secondPage.pack()


# widgets of Home Page
Label(homePage, text="โปรแกรมจำแนกหิน", style="header.TLabel").pack(
    side=tk.TOP, expand=True)
Button(homePage, text="จำแนกหิน", style="TButton", command=startForm).pack(
    side=tk.TOP, expand=True)
Button(homePage, text="ผู้จัดทำ", style="TButton", command=lambda: changePage(
    homePage, authorPage)).pack(side=tk.TOP, expand=True)
Button(homePage, text="ผังงาน", style="TButton", command=lambda: webbrowser.open(
    FLOWCHART_URL)).pack(side=tk.TOP, expand=True)
Button(homePage, text="ออก", style="TButton",
       command=root.destroy).pack(side=tk.TOP, expand=True)

# widgets of Author Page
Label(authorPage, text="จัดทำโดย", style="header.TLabel").pack(side=tk.TOP)
Label(authorPage, image=authorImage).pack(side=tk.TOP, expand=True)
Label(authorPage, text="นายธนกร  แสงจันทร์",
      style="body.TLabel").pack(side=tk.TOP, expand=True)
Label(authorPage, text="เลขที่ 9 ชั้นมัธยมศึกษาปีที่ 4/1 (โอเมก้า)",
      style="body.TLabel").pack(side=tk.TOP, expand=True)
Button(authorPage, text="ออก", style="TButton", command=lambda: changePage(
    authorPage, homePage)).pack(side=tk.BOTTOM, expand=False)
Separator(authorPage, orient="horizontal").pack(
    side=tk.BOTTOM, fill=tk.X, pady=20)

# Start Program
homePage.pack()
root.geometry("720x480+400+150")
root.title("โปรแกรมจำแนกหิน")
root.mainloop()
