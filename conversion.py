import xmltodict
import pandas as pd
import datetime
import pytz


def get_datas(xml, values):

  with open(f"xml/{xml}", 'rb') as file:
    dict_file = xmltodict.parse(file)

    try:
      if "NFe" in dict_file:
        info_invoice = dict_file["NFe"]["infNFe"]
      else:
        info_invoice = dict_file["nfeProc"]["NFe"]["infNFe"]

      invoice = info_invoice["@Id"]
      company_name = info_invoice["emit"]["xNome"]
      company_cnpj = info_invoice["emit"]["CNPJ"]
      address = info_invoice["emit"]["enderEmit"]

      if "vol" in info_invoice["transp"]:
        weight = info_invoice["transp"]["vol"]["pesoB"]
      else:
        weight = "weight value not informed"

      values.append([invoice, company_name, company_cnpj, address, weight])
    except Exception as e:
      with open('log_error.txt', 'a') as file_log:
              time_zone = pytz.timezone("America/Sao_Paulo")
              date = datetime.datetime.now().astimezone(time_zone).strftime("%d/%m/%Y - %H:%Mh")
              file_log.write(f'\n{date} - Error in get file data {xml}. Error: {e}')

def create_table(values):

  columns = ["invoice", "company_name", "company_cnpj", "address", "weight"]
  
  table = pd.DataFrame(columns=columns, data=values)
  table.to_excel("Invoices.xlsx", index=False)

  print("File created!")