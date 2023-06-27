import csv
import xml.etree.ElementTree as ET

def export_votable_to_csv(xml_file, csv_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    
    namespace = {'vot': 'http://www.ivoa.net/xml/VOTable/v1.3'}

   
    table = root.find('vot:RESOURCE/vot:TABLE', namespace)

   
    fields = [field.attrib['name'] for field in table.findall('vot:FIELD', namespace)]

    
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(fields)

       
        for row in table.findall('vot:DATA/vot:TABLEDATA/vot:TR', namespace):
            values = [element.text for element in row.findall('vot:TD', namespace)]
            writer.writerow(values)


xml_file = 'C:\\LOCAL\\Cone_gaiadr3.gaia_source_[56.601,24.114]_5.0.vot'
csv_file = 'C:\\LOCAL\\data_pleiades.csv'
export_votable_to_csv(xml_file, csv_file)
