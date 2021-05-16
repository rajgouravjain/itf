## itf


#Command to run pytest on remote server behind jumphost

```sh
#!/bin/bash
python3 -m pytest -n 3  --ssh-config=/Users/rajgouravj/.ssh/oregon_config --ssh-identity-file=/Users/rajgouravj/.ssh/Developerv2.pem   --hosts=ec2-user@172.29.0.25 --junitxml=junit.xml tests/integration/testinfra/elasticsearch_cluster/
```

```sh
pytest -n 3 -vvv --sudo       --ssh-config=/Users/rajgouravj/.ssh/zendrive_oregon_config --ssh-identity-file=/Users/rajgouravj/.ssh/DeveloperV2.pem   --hosts=ssh://ubuntu@172.19.10.165 --junitxml=/tmp/junit.xml elasticsearch_cluster/
```
