import pandas as pd

# 1. โหลดข้อมูลจากไฟล์
sap_df = pd.read_csv(&#39;EXPORT SAP 22.04.69.XLSX - Sheet1.csv&#39;)
dmsx_df = pd.read_csv(&#39;EXPORT DMSX 22.04.69.xlsx - DMSX.csv&#39;, skiprows=3)

# ... (วาง Code ที่เหลือทั้งหมดตรงนี้) ...

print(mismatched)