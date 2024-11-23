### Task #1. MinIO cluster
Set up a distributed cluster with 3 MinIO nodes, ensuring each node runs as a
separate systemd unit service using docker container(-s).
Verify that data is properly distributed and replicated across all nodes. Simulate
node failures to confirm data availability and resilience under various conditions.

``` bash
docker pull minio/minio:latest

docker network create minio-network

mkdir -p ~/minio/node1/disk{1..4}
mkdir -p ~/minio/node2/disk{1..4}
mkdir -p ~/minio/node3/disk{1..4}
```

systemd 
```bash
sudo vim /etc/systemd/system/minio@.service
```
``` bash
[Unit]
Description=MinIO Cluster Node %i
After=network.target docker.service
Requires=docker.service

[Service]
EnvironmentFile=/etc/default/minio
ExecStartPre=-/usr/bin/docker stop minio%i
ExecStartPre=-/usr/bin/docker rm minio%i
ExecStartPre=/usr/bin/docker pull minio/minio:latest
ExecStart=/usr/bin/docker run --rm \
  --name minio%i \
  --network minio-network \
  -p 900%i:9000 \
  -v /home/aral/minio/node%i/disk1:/data1 \
  -v /home/aral/minio/node%i/disk2:/data2 \
  -v /home/aral/minio/node%i/disk3:/data3 \
  -v /home/aral/minio/node%i/disk4:/data4 \
  -e MINIO_ROOT_USER=yourusername \
  -e MINIO_ROOT_PASSWORD=pass \
  minio/minio server http://minio1:9000/data1 \
                         http://minio2:9000/data1 \
                         http://minio3:9000/data1 \
                         http://minio1:9000/data2 \
                         http://minio2:9000/data2 \
                         http://minio3:9000/data2 \
                         http://minio1:9000/data3 \
                         http://minio2:9000/data3 \
                         http://minio3:9000/data3 \
                         http://minio1:9000/data4 \
                         http://minio2:9000/data4 \
                         http://minio3:9000/data4

Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target

```
```bash
sudo systemctl daemon-reload

sudo systemctl start minio@1
sudo systemctl start minio@2
sudo systemctl start minio@3

sudo systemctl enable minio@1
sudo systemctl enable minio@2
sudo systemctl enable minio@3

sudo systemctl status minio@1
sudo systemctl status minio@2
sudo systemctl status minio@3
```
### go to 172.19.0.2:9000
in health we can see 3 nodes and 3 drivers
![image](https://github.com/user-attachments/assets/f4657349-67cb-41fa-b0ff-8a3b10d024ea)



```bash
wget https://dl.min.io/client/mc/release/linux-amd64/mc
chmod +x mc
sudo mv mc /usr/local/bin/
mc --version
```

``` bash
mc alias set node1 http://127.0.0.1:9001 YOURROOTUSER YOURROOTPASSWORD
mc alias set node2 http://127.0.0.1:9002 YOURROOTUSER YOURROOTPASSWORD
mc alias set node3 http://127.0.0.1:9003 YOURROOTUSER YOURROOTPASSWORD
```
info about nodes
``` bash
mc admin info node1
mc admin info node2
mc admin info node3
```
data verification and heal lost data:
``` bash
mc admin heal info node1
mc admin heal info node2
mc admin heal info node3
```

new bucket
``` bash
mc mb node1/test
```
auto heal
```bash
mc admin heal --recursive node1/testbucket
mc admin heal --recursive node2/testbucket
mc admin heal --recursive node3/testbucket
```

## Verify that data is properly distributed and replicated across all nodes. Simulate
node failures to confirm data availability and resilience under various conditions.
``` bash
sudo systemctl stop minio@1
```

check that another nodes are avaliaable
``` bash
mc ls node2/test
mc ls node3/test
```
add data to nodes
``` bash
mc cp /path/to/local/file4 node2/testbucket/
mc cp /path/to/local/file5 node3/testbucket/
```

``` bash
sudo systemctl start minio@1

mc admin info node1
mc admin info node2
mc admin info node3
```
to check data distribution
```bash
mc ls node1/testbucket
mc ls node2/testbucket
mc ls node3/testbucket
```

### data distribution demonstration

[Screencast from 23.11.2024 21:00:50.webm](https://github.com/user-attachments/assets/14f04ef0-51c7-4d48-9e02-1e2069fca924)

### node failure demonstration

[Screencast from 23.11.2024 21:38:07.webm](https://github.com/user-attachments/assets/80760806-c63e-4d33-ac9a-615deda999be)

[Screencast from 23.11.2024 21:51:28.webm](https://github.com/user-attachments/assets/6f571170-5ed9-4979-b118-b1df35782c9b)
