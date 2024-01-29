import xlsxwriter
from parsing_website import get_info_product


def writer(data_product, row=0, column=0):
    """Функция записи собранной информации по товару в файл Excel"""
    # Создаем/открываем файл Excel
    book = xlsxwriter.Workbook('Перечень товара.xlsx')
    # Создаем рабочий лист в Excel файле
    page = book.add_worksheet('Товар')

    # Запускаем цикл по полученному кортежу данных в рамках собранной информации
    for item in data_product():
        for index in range(4):
            # Осуществляем построчную запись текстовых данных по каждому товару
            page.write(row, column + index, item[index])
        # Осуществляем построчную запись изображения для каждого товара
        page.insert_image(row, 4, 'image_product\\' + item[0] + '_' + item[3].split('/')[-1],
                          {'x_offset': 5, 'y_offset': 5, 'x_scale': 0.1, 'y_scale': 0.09})
        # Осуществляем ручную настройку высоты ячеек
        page.set_row(row, 90)
        row += 1

    # Осуществляем автоматическую настройку ширины ячеек
    page.autofit()
    # Осуществляем ручную настройку ширины ячейки и автоматического переноса текста
    page.set_column('C:C', 40, book.add_format({'text_wrap': True}))
    # Осуществляем ручную настройку ширины ячейки
    page.set_column('E:E', 15)
    book.close()


print('Осуществляется загрузка данных с сайта, дождитесь окончания выполнения программы...')
writer(get_info_product)
print('Данные успешно загружены в файл - Перечень товара.xlsx')
