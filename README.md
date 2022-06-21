#Infrastructure testing environment setup 

- download and install ruby
- install ```bundler``` 
- create Gemfile with following contents in directory where kitchen is required. In this case its preprod env :: 
```
source "https://rubygems.org"

gem "rake"
gem 'nokogiri'
gem 'rspec', :require => 'spec'
gem "test-kitchen"
gem "kitchen-ansible"
gem 'kitchen-inspec'
gem 'inspec'
gem 'serverspec'
gem 'awspec'
gem "rubyzip", ">= 1.3.0"
gem "mixlib-shellout"```
gem "kitchen-verifier-serverspec"
gem 'kitchen-docker', :git => 'https://github.com/test-kitchen/kitchen-docker.git'
```
- run ```BUNDLE_GEMFILE=Gemfile bundler install``` command to install all packages.
- setup .kitchen.yml file
- run following commands ::
```sh 
bundler exec kitchen create basic-ubuntu-2004
```
```sh 
bundler exec kitchen converge basic-ubuntu-2004
```
```sh 
bundler exec kitchen verify basic-ubuntu-2004
```


=======
## itf


#Command to run pytest on remote server behind jumphost

```sh
#!/bin/bash
python3 -m pytest -n 3  --ssh-config=/Users/rajgouravj/.ssh/oregon_config --ssh-identity-file=/Users/rajgouravj/.ssh/Developerv2.pem   --hosts=ec2-user@172.29.0.25 --junitxml=junit.xml server-verify-root/tests/integration/basic/testinfra/elasticsearch_cluster/
```

```sh
pytest -n 3 -vvv --sudo       --ssh-config=/Users/rajgouravj/.ssh/zendrive_oregon_config --ssh-identity-file=/Users/rajgouravj/.ssh/DeveloperV2.pem   --hosts=ssh://ubuntu@172.19.10.165 --junitxml=/tmp/junit.xml server-verify-tests/integration/basic/testinfra/elasticsearch_cluster/
```
