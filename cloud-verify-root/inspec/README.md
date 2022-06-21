#Install inspec using command
```
curl https://omnitruck.chef.io/install.sh | sudo bash -s -- -P inspec
```

# TO create a inspec profile
```
inspec init profile --platform=aws aws_verify
```

# To run the inspec profile
```
inspec exec aws_verify -t aws://
```
