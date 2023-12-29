import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse("bai2.3.xml");
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    staff_list = doc.getElementsByTagName("staff");
    print('%d staff:' % staff_list.length)
    for staff in staff_list:
        staff_id = staff.getAttribute("id")
        name = staff.getElementsByTagName("name")[0].childNodes[0].data # trả về ptử đầu và truy cập node con đầu tiên
        salary = staff.getElementsByTagName("salary")[0].childNodes[0].data
        print("\n staff id:",staff_id)
        print("\n name:",name)
        print("\n salary:",salary)


if __name__ == '__main__':
    main();
