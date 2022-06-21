require 'spec_helper'

describe vpc('ireland_prd') do
  it { should exist }
  it { should be_available }
  its(:vpc_id) { should eq 'vpc-09e196996413' }
  its(:cidr_block) { should eq '10.9.0.0/16' }
  it { should have_route_table('ireland_prd_private_eu-west-1b') }
  it { should have_route_table('ireland_prd_public_route_table') }
  it { should have_route_table('rtb-0d5edac8ad6f9') }
  it { should have_route_table('ireland_prd_private_eu-west-1a') }
  it { should have_network_acl('acl-0bcd67b60888b') }
  it { should have_vpc_attribute('enableDnsHostnames') }
  it { should have_vpc_attribute('enableDnsSupport') }
end
