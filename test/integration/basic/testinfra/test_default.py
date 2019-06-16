def test_file_present(host):
  file = host.file("/tmp/hello.txt")
  assert(file.exists)
def test_file_contents(host):
  file = host.file("/tmp/hello.txt")
  assert(file.content_string == "Hello world!")
