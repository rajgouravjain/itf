# copyright: 2018, Rajgourav Jain

title "Hello world"

describe file("/tmp") do
  it { should be_directory }
end

# you add controls here
control "tmp-1.0" do                        # A unique ID for this control
  impact 0.7                                # The criticality, if this control fails.
  title "Create /tmp/hello.txt file"             # A human-readable title
  desc "Verifing hello.txt file"
  describe file("/tmp/hello.txt") do                  # The actual test
    it { should be_file }
    its(:content) { should match(/Hello world!/) }
  end
end
