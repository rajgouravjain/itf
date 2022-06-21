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



There are multiple  ways infra can be tested

## Infra testing using awspec
- Best way to testing using awspec
```
bundle exec rspec tests/integration/ireland-eu-west-1/sqs/
```


- Another way is you maintain a Rakefile and run following commands. All test cases must be in spec directory.
```
bundle exec rake spec

