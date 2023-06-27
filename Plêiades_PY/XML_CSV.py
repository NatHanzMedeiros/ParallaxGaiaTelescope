import csv
import xml.etree.ElementTree as ET

def export_votable_to_csv(xml_file, csv_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Encontra o namespace do VOTable
    namespace = {'vot': 'http://www.ivoa.net/xml/VOTable/v1.3'}

    # Encontra o elemento TABLE dentro do VOTable
    table = root.find('vot:RESOURCE/vot:TABLE', namespace)

    # Obtém os nomes dos campos (colunas)
    fields = [field.attrib['name'] for field in table.findall('vot:FIELD', namespace)]

    # Cria o arquivo CSV e escreve o cabeçalho
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(fields)

        # Extrai os valores dos campos de cada linha e escreve no CSV
        for row in table.findall('vot:DATA/vot:TABLEDATA/vot:TR', namespace):
            values = [element.text for element in row.findall('vot:TD', namespace)]
            writer.writerow(values)

# Exemplo de uso
xml_file = 'C:\\Users\\nathan\\Documents\\Cone_gaiadr3.gaia_source_[56.601,24.114]_5.0.vot'
csv_file = 'C:\\Users\\nathan\\Documents\\data_pleiades.csv'
export_votable_to_csv(xml_file, csv_file)
