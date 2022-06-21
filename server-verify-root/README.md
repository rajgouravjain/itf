#Infrastructure testing environment setup 

- download and install ruby
- install ```bundler``` 
- create Gemfile with following contents in directory where kitchen is required. In this case its preprod env :: 
```
source "https://rubygems.org"
gem "test-kitchen"
gem "kitchen-ansible"
gem "serverspec"
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
