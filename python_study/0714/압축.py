import zipfile

filelist=['./0714/data.data','./0714/test.csv']
with zipfile.ZipFile('./0714/test.zip','w') as myzip:
    for temp in filelist:
        myzip.write(temp)

zipfile.ZipFile("./0714/test.zip").extractall()