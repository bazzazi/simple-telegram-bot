from datetime import datetime

def Responses(text):
    text=str(text).lower()
    if text in ("تاریخ", "تاریخ؟"):
        now=datetime.now()
        date=now.strftime("%Y/%m/%d, %H:%M:%S")
        return date
    elif text in ("سلام","سلام!"):
        return "سلام، روز خوبی داشته باشی"
    elif text in ("تو کی هستی","تو کی هستی؟"):
        return "من ربات هستم"
    elif text in ("چن سالته","چند سالته؟"):
        return "من 20 سالمه"
    else:
        return "متوجه منظورتون نشدم"