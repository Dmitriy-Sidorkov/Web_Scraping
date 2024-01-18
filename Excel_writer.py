import xlsxwriter
from first_step import get_info_product


def writer(data_product, row=0, column=0):
    book = xlsxwriter.Workbook('Перечень товара.xlsx')
    page = book.add_worksheet('Товар')

    page.set_column('A:A', 20)
    page.set_column('B:B', 20)
    page.set_column('C:C', 50)
    page.set_column('D:D', 50)

    for item in data_product():
        for index in range(4):
            page.write(row, column + index, item[index])
        row += 1

    book.close()


writer(get_info_product)
