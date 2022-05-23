import xml.etree.ElementTree as ET
import os


# функция возвращает список .xml файлов из папки, включая подпапки, кроме proto_.xml
def get_file_list(path):
    filelist = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".xml") and file != "proto_.xml":
                filelist.append(os.path.join(root, file))
    # print(filelist)  #  Проверка пути!!!!!!!!!!!!!!!!
    return filelist


# MIF        Функция парсит кпт и вытаскивает количество контуров, количество точек и их координаты
def make_list_for_mif_actual_land(file_name):
    list_land = []
    tree = ET.parse(file_name)
    # возвращает список участков
    land_records = tree.findall('cadastral_blocks/cadastral_block/record_data/base_data/land_records/land_record')
    for land_record in land_records:
        # возвращает список контуров в каждом участке
        spatal_elements = land_record.findall("./contours_location/contours/contour/entity_spatial/"
                                              "spatials_elements/spatial_element")
        list_land.append("Region ")
        list_land.append(len(spatal_elements))
        for spatal_element in spatal_elements:
            # возвращает список координат точек в каждом контуре в каждом участке
            ordinates = spatal_element.findall("./ordinates/ordinate")
            list_land.append(len(ordinates))
            # возращаем значение координат из списка
            for ordinate in ordinates:
                y = ordinate.find('y').text
                x = ordinate.find('x').text
                list_land.append(y)
                list_land.append(x)
    return list_land


# MIF Функция печатает в файл mif заголовочные данные
def print_head_mif():
    file_mif_head = open('actual_land.mif', 'a')
    head_data = [
        'Version   450',
        'Charset "WindowsCyrillic"',
        'Delimiter ","',
        'CoordSys Earth Projection 8, 1001, "m", 88.466666, 0, 1, 2300000, -5512900.5630000001 '
        'Bounds (-5949281.53901, -15515038.0608) (10549281.539, 4489236.93476)',
        'Columns 8',
        'type Char(30)',
        'cad_number Char(30)',
        'readable_address Char(254)',
        'permitted_use Char(254)',
        'area Char(50)',
        'cost Char(50)',
        'category Char(50)',
        'date_download Char(10)',
        'Data'
        ]
    for index in head_data:
        file_mif_head.write(index + '\n')
    file_mif_head.close()


def make_list_for_mid_actual_land(file_name):
    list_semantic_land = []
    list_type_land_record = []
    list_cad_number = []
    list_readable_address = []
    list_permitted_use = []
    list_area = []
    list_cost = []
    list_category = []
    list_request = []
    tree = ET.parse(file_name)
    root = tree.getroot()

    data = tree.findall('cadastral_blocks/cadastral_block/record_data/base_data/land_records/land_record')
    for data1 in data:
        data2 = data1.findall('./object/common_data/type/value')
        for type in data2:
            _type = type.text
            print(_type)
        data3 = data1.findall('./object/common_data/cad_number')
        for cad_number in data3:
            print(cad_number.text)
        data4 = data1.findall('./address_location/address/readable_address')
        for adress in data4:
            print(adress.text)
        data5 = data1.findall('params/permitted_use/permitted_use_established/by_document')
        for permitted_use in data5:
            print(permitted_use.text)
        data6 = data1.findall('params/area/value')
        for area in data6:
            print(area.text)
        date6 = data1.findall('./cost/value')
        if len(date6) >= 1:
            for cost in date6:
                _cost = cost.text
        else:
            _cost = "None"
        print(_cost)
        date7 = data1.findall('params/category/type/value')
        for category in date7:
            print(category.text)
        request = root[1][0].text
        print(request)



    # file_mid = open('actual_land.mid', 'a')
    # i = 0
    # while i < len(list_type_land_record):
    #     a = ("\"" + list_type_land_record[i] + "\","
    #          + "\"" + list_cad_number[i] + "\","
    #          + "\"" + list_readable_address[i] + "\","
    #          + "\"" + list_permitted_use[i] + "\","
    #          + "\"" + list_area[i] + "\","
    #          + "\"" + list_cost[i] + "\","
    #          + "\"" + list_category[i] + "\","
    #          + "\"" + list_request[i] + "\"")
    #     file_mid.write(a + '\n')
    #     i += 1
    #     print(i)
    # file_mid.close()
    # print(len(list_type_land_record))
    # print(len(list_cad_number))
    # print(len(list_readable_address))
    # print(len(list_permitted_use))
    # print(len(list_area))
    # print(len(list_cost))
    # print(len(list_category))
    # print(len(list_request))

    return list_semantic_land


if __name__ == '__main__':
    # print_head_mif()
    # filelist = get_file_list("C:/Users/Necvetaeva_v/PycharmProjects/ParserXML/materials/23.05.2022_12_32_выгрузка/Новая папка")
    filelist = get_file_list("D:\project_Python\ParserXML\materials\_Level1")
    # Открываем поочередно кпт.xml файлы
    for file_name in filelist:
        # file_mif = open('actual_land.mif', 'a')
        # list_coordinate_land_record = make_list_for_mif_actual_land(file_name)
        # # дозаписываем полученный список в файл
        # for data8 in list_coordinate_land_record:
        #    file_mif.write(str(data8) + '\n')
        # file_mif.close()
        make_list_for_mid_actual_land(file_name)

