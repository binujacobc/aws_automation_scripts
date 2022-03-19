from datetime import datetime, timedelta
import datetime
import sys
import os
import boto3
def lambda_handler(event, context):
    try:
       s3 = boto3.resource('s3')
       bucketname = os.environ['BucketName']
       folder = os.environ['Folder']
       retaildays = os.environ['Retaindays']
       bucket = s3.Bucket(bucketname)
       past = ((str((datetime.datetime.now() - timedelta(days=int(retaildays))).date())).replace('-', ',')).split (",")
       for obj in bucket.objects.filter(Prefix=folder):
            if (obj.last_modified).replace(tzinfo = None) < datetime.datetime(int(past[0]),int(past[1]),int(past[2])):
                if (obj.key).endswith(folder):
                    continue
                else:
                    print('The following files are deleting....')
                    print('File Name: %s :: Date: %s' % (obj.key,obj.last_modified))
                    obj.delete()
            else:
                print("No files to delete")
    except Exception as e:
        print(e)
