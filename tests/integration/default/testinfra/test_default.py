def test_file_present(host):
  file = host.file("/etc/passwd")
  assert(file.exists)
