How to upload and process the Excel file in Django

If you are setting up a new project then create a new virtual environment and install Django and openpyxl modules in virtual environment using pip.

```python
pip install Django
pip install openpyxl
```

URLs:
Add a URL in urls.py file of app.

```python
excelupload_patterns = [
    path("material_upload", MaterialUpload.as_view(), name="material_upload"),
]
```

```python
    def post(self, request):
        form = UploadMaterialsForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES["material_upload_file"]
            # you may put validations here to check extension or file size
            wb = openpyxl.load_workbook(excel_file)
            worksheet = wb["Sheet1"]
            excel_data = list()
            # iterating over the rows and
            # getting value from each cell in row
            cnt = 0
            for row in worksheet.iter_rows():
                row_heading = list()
                if cnt == 0:
                    material_heading = ['Code', 'Name', 'Description', 'Type', 'Category', 'Unit', 'VAT', 'SD',
                                        'Tax Year', 'HS Code']
                    for cell in row:
                        row_heading.append(str(cell.value))
                    cnt = cnt + 1
                    material_heading = list(map(str.lower, material_heading))
                    row_heading = list(map(str.lower, row_heading))

                    if row_heading == material_heading:
                        pass
                    else:
                        messages.error(request, 'Excel Row Headers Mismatch..', extra_tags='alert-danger')
                        return redirect('')

                else:
                    row_data = list()
                    for cell in row:
                        row_data.append(str(cell.value))

                    material = Material()
                    code = row_data[0]
                    name = row_data[1]
                    description = row_data[2]
                    unit = row_data[3]
                    material_type = row_data[4]
                    material_category = row_data[4]
                    tax_type = row_data[5]
                    sd_type = row_data[6]
                    tax_year = row_data[7]
                    hscode = row_data[8]

                    return HttpResponse(material_type)
                    # excel_data.append(row_data)

            messages.success(request, 'Material Uploaded Successfully..', extra_tags='alert-success')
            return redirect(' ')
        else:
            return render(request, 'excelupload/upload_materials.html', {'form': form})
```

