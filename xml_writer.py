from lxml import etree


class XmlWriter:
    @staticmethod
    def write_to_mysql_format(rows):
        root_element = etree.Element("resultset")
        for row in rows:
            row_element = etree.Element("row")
            row_element.append(XmlWriter.__create_field__("date", row["date"]))
            row_element.append(XmlWriter.__create_field__("amount", row["amount"]))
            row_element.append(XmlWriter.__create_field__("cost", row["cost"]))
            root_element.append(row_element)
        et = etree.ElementTree(root_element)
        et.write('test.xml', pretty_print=True, xml_declaration=True, encoding="utf-8")

    @staticmethod
    def __create_field__(name, value):
        field = etree.Element("field", name=name)
        field.text = value
        return field
