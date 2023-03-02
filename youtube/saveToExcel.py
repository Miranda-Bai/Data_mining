from openpyxl import Workbook

wb= Workbook()
ws = wb.active
ws.append(["title","url"])
wb.save("youtube.xlsx")