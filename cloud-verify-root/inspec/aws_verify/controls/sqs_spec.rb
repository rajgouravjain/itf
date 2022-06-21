describe aws_sqs_queue('new_sqs_queue') do
  it { should exist }
  its('visibility_timeout') { should be 300 }
end
