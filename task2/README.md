##Task #2. Data synchronization

Synchronize data between your local system and MinIO bucket. Ensure that a
bucket is created in MinIO (if it does not already exist) to act as the target for
synchronization.

Configure the synchronization process to run between your local system and the
MinIO bucket every minute.

For additional assistance, refer to https://rclone.org/

### Instructions

1. Install rclone

2. create config for rclone
```bash
rclone config

Option provider.
Choose your S3 provider.
Choose a number from below, or type in your own value of type string.
Press Enter for the default (Minio).
 1 / Amazon Web Services (AWS) S3
   \ (AWS)
 2 / Alibaba Cloud Object Storage System (OSS) formerly Aliyun
   \ (Alibaba)
 3 / Arvan Cloud Object Storage (AOS)
   \ (ArvanCloud)
 4 / Ceph Object Storage
   \ (Ceph)
 5 / China Mobile Ecloud Elastic Object Storage (EOS)
   \ (ChinaMobile)
 6 / Cloudflare R2 Storage
   \ (Cloudflare)
 7 / DigitalOcean Spaces
   \ (DigitalOcean)
 8 / Dreamhost DreamObjects
   \ (Dreamhost)
 9 / Google Cloud Storage
   \ (GCS)
10 / Huawei Object Storage Service
   \ (HuaweiOBS)
11 / IBM COS S3
   \ (IBMCOS)
12 / IDrive e2
   \ (IDrive)
13 / IONOS Cloud
   \ (IONOS)
14 / Seagate Lyve Cloud
   \ (LyveCloud)
15 / Leviia Object Storage
   \ (Leviia)
16 / Liara Object Storage
   \ (Liara)
17 / Linode Object Storage
   \ (Linode)
18 / Magalu Object Storage
   \ (Magalu)
19 / Minio Object Storage
   \ (Minio)
20 / Netease Object Storage (NOS)
   \ (Netease)
21 / Petabox Object Storage
   \ (Petabox)
22 / RackCorp Object Storage
   \ (RackCorp)
23 / Rclone S3 Server
   \ (Rclone)
24 / Scaleway Object Storage
   \ (Scaleway)
25 / SeaweedFS S3
   \ (SeaweedFS)
26 / StackPath Object Storage
   \ (StackPath)
27 / Storj (S3 Compatible Gateway)
   \ (Storj)
28 / Synology C2 Object Storage
   \ (Synology)
29 / Tencent Cloud Object Storage (COS)
   \ (TencentCOS)
30 / Wasabi Object Storage
   \ (Wasabi)
31 / Qiniu Object Storage (Kodo)
   \ (Qiniu)
32 / Any other S3 compatible provider
   \ (Other)
provider> 19

Option env_auth.
Get AWS credentials from runtime (environment variables or EC2/ECS meta data if no env vars).
Only applies if access_key_id and secret_access_key is blank.
Choose a number from below, or type in your own boolean value (true or false).
Press Enter for the default (false).
 1 / Enter AWS credentials in the next step.
   \ (false)
 2 / Get AWS credentials from the environment (env vars or IAM).
   \ (true)
env_auth> 1

Option access_key_id.
AWS Access Key ID.
Leave blank for anonymous access or runtime credentials.
Enter a value of type string. Press Enter for the default (aral123).
access_key_id> aral123

Option secret_access_key.
AWS Secret Access Key (password).
Leave blank for anonymous access or runtime credentials.
Enter a value of type string. Press Enter for the default (pass123123).
secret_access_key> pass123123

Option region.
Region to connect to.
Leave blank if you are using an S3 clone and you don't have a region.
Choose a number from below, or type in your own value of type string.
Press Enter for the default (us-east-1).
   / Use this if unsure.
 1 | Will use v4 signatures and an empty region.
   \ ()
   / Use this only if v4 signatures don't work.
 2 | E.g. pre Jewel/v10 CEPH.
   \ (other-v2-signature)
region> 

Option endpoint.
Endpoint for S3 API.
Required when using an S3 clone.
Enter a value of type string. Press Enter for the default (http://127.0.0.1:9000).
endpoint> http://172.19.0.3:9000

Option location_constraint.
Location constraint - must be set to match the Region.
Leave blank if not sure. Used when creating buckets only.
Enter a value. Press Enter to leave empty.
location_constraint> 

Option acl.
Canned ACL used when creating buckets and storing or copying objects.
This ACL is used for creating objects and if bucket_acl isn't set, for creating buckets too.
For more info visit https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl
Note that this ACL is applied when server-side copying objects as S3
doesn't copy the ACL from the source but rather writes a fresh one.
If the acl is an empty string then no X-Amz-Acl: header is added and
the default (private) will be used.
Choose a number from below, or type in your own value of type string.
Press Enter for the default (private).
   / Owner gets FULL_CONTROL.
 1 | No one else has access rights (default).
   \ (private)
   / Owner gets FULL_CONTROL.
 2 | The AllUsers group gets READ access.
   \ (public-read)
   / Owner gets FULL_CONTROL.
 3 | The AllUsers group gets READ and WRITE access.
   | Granting this on a bucket is generally not recommended.
   \ (public-read-write)
   / Owner gets FULL_CONTROL.
 4 | The AuthenticatedUsers group gets READ access.
   \ (authenticated-read)
   / Object owner gets FULL_CONTROL.
 5 | Bucket owner gets READ access.
   | If you specify this canned ACL when creating a bucket, Amazon S3 ignores it.
   \ (bucket-owner-read)
   / Both the object owner and the bucket owner get FULL_CONTROL over the object.
 6 | If you specify this canned ACL when creating a bucket, Amazon S3 ignores it.
   \ (bucket-owner-full-control)
acl> 1

Option server_side_encryption.
The server-side encryption algorithm used when storing this object in S3.
Choose a number from below, or type in your own value.
Press Enter to leave empty.
 1 / None
   \ ()
 2 / AES256
   \ (AES256)
 3 / aws:kms
   \ (aws:kms)
server_side_encryption> 1

Option sse_kms_key_id.
If using KMS ID you must provide the ARN of Key.
Choose a number from below, or type in your own value.
Press Enter to leave empty.
 1 / None
   \ ()
 2 / arn:aws:kms:*
   \ (arn:aws:kms:us-east-1:*)
sse_kms_key_id> 1

Edit advanced config?
y) Yes
n) No (default)
y/n> n

Configuration complete.
Options:
- type: s3
- provider: Minio
- access_key_id: aral123
- secret_access_key: pass123123
- region: us-east-1
- endpoint: http://172.19.0.3:9000
- acl: private
Keep this "minio" remote?
y) Yes this is OK (default)
e) Edit this remote
d) Delete this remote
y/e/d> y

Current remotes:

Name                 Type
====                 ====
minio                s3

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> q

```


my config 
```bash
aral@aral-ROG-Strix-G513RM-G513RM:~/minio/node1$ rclone config
Current remotes:

Name                 Type
====                 ====
minio                s3

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> e

Select remote.
Choose a number from below, or type in an existing value.
 1 > minio
remote> 1

Editing existing "minio" remote with options:
- type: s3
- provider: Minio
- access_key_id: aral123
- secret_access_key: pass123123
- region: us-east-1
- endpoint: http://127.0.0.1:9000
- acl: private
```


Commands 
List buckets

    rclone lsd minio:

Make a new bucket

    rclone mkdir minio:bucket

Sync files into that bucket - try with `--dry-run` first

    rclone --size-only --dry-run sync /path/to/files minio:bucket

Then sync for real

    rclone --size-only sync /path/to/files minio:bucket


    rclone sync minio:test /home/aral/minio-backup
    mc mirror local/test /home/aral/minio/node1/disk1/test 

### Note: dont use path to real minio
aral@aral-ROG-Strix-G513RM-G513RM:~/minio/node1$ ls
disk1  disk2  disk3  disk4
dont use this path, will be Access denied

minio/node1/disk1/... — это внутренние каталоги MinIO, где сервер хранит свои данные и метаданные. Эти файлы не предназначены для ручного копирования обратно в MinIO через S3 API. При попытке загрузить эти внутренние служебные файлы через rclone вы, пытаетесь сохранить уже существующую внутреннюю структуру MinIO в тот же или другой бакет. MinIO защищает эти структуры и не даёт переписывать метаданные таким образом. Отсюда и Access Denied.


### Note 2: if you want to create policies there may be error like
```bash
aral@aral-ROG-Strix-G513RM-G513RM:~/minio/node1/disk1/test3$ mc admin policy attach local writeonly --user aral123
mc: <ERROR> Unable to make user/group policy association. Specified IAM action is not allowed.
```
then do this
mc alias set local http://172.19.0.3:9000 aral123 pass123123


## [Script for sync](syns_minio_rclone.sh)

Usage Script
```bash
chmod +x syns_minio_rclone.sh
./syns_minio_rclone.sh BUCKET_NAME
```

Create cron
```bash
crontab -e
```
write at the end command like
```bash
* * * * * /home/aral/gitREPOS/minio/task2/syns_minio_rclone.sh test
```
to run script every minute

Then check logs
```bash
aral@aral-ROG-Strix-G513RM-G513RM:~/minio-backup/logs$ cat minio-test-sync.log 
2024/12/06 10:10:01 INFO  : There was nothing to transfer
2024/12/06 10:10:01 INFO  : 
Transferred:   	          0 B / 0 B, -, 0 B/s, ETA -
Checks:                 2 / 2, 100%
Elapsed time:         0.0s

2024/12/06 10:11:01 INFO  : There was nothing to transfer
2024/12/06 10:11:01 INFO  : 
Transferred:   	          0 B / 0 B, -, 0 B/s, ETA -
Checks:                 2 / 2, 100%
Elapsed time:         0.0s

2024/12/06 10:12:01 INFO  : There was nothing to transfer
2024/12/06 10:12:01 INFO  : 
Transferred:   	          0 B / 0 B, -, 0 B/s, ETA -
Checks:                 2 / 2, 100%
Elapsed time:         0.0s

2024/12/06 10:13:01 INFO  : There was nothing to transfer
2024/12/06 10:13:01 INFO  : 
Transferred:   	          0 B / 0 B, -, 0 B/s, ETA -
Checks:                 2 / 2, 100%
Elapsed time:         0.0s

2024/12/06 10:14:01 INFO  : There was nothing to transfer
2024/12/06 10:14:01 INFO  : 
Transferred:   	          0 B / 0 B, -, 0 B/s, ETA -
Checks:                 2 / 2, 100%
Elapsed time:         0.0s

2024/12/06 10:14:09 INFO  : There was nothing to transfer
2024/12/06 10:14:09 INFO  : 
Transferred:   	          0 B / 0 B, -, 0 B/s, ETA -
Checks:                 2 / 2, 100%
Elapsed time:         0.0s

2024/12/06 10:15:01 INFO  : There was nothing to transfer
2024/12/06 10:15:01 INFO  : 
Transferred:   	          0 B / 0 B, -, 0 B/s, ETA -
Checks:                 2 / 2, 100%
Elapsed time:         0.0s
```
