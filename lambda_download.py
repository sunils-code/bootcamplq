import boto3, zipfile, urllib.request
from io import BytesIO

def lambda_handler(event, context):
   s3bucketname = "nrttestbucket1"
   filename = "photogenic.zip"
   localpath = "/tmp/"
   tmpfile = localpath + filename
   s3_path = "zipfolder/" + filename
   urlpath = "https://github.com/neiltucker/awssaa/raw/main/photogenic.zip"
   urllib.request.urlretrieve(urlpath, tmpfile)
   s3 = boto3.resource('s3')
   s3bucket = s3.Bucket(s3bucketname)
   s3.meta.client.upload_file(tmpfile,s3bucketname,s3_path)
   for file in s3bucket.objects.all():
     if(str(file.key).endswith('.zip')):
       zip_obj = s3.Object(s3bucketname,file.key)
       buffer = BytesIO(zip_obj.get()["Body"].read())

       zfile = zipfile.ZipFile(buffer)
       for file in zfile.namelist():
         file_info= zfile.getinfo(file)
         response = s3.meta.client.upload_fileobj(zfile.open(file),s3bucketname,file)

