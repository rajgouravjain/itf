import pytest
import sys

path="/data"

@pytest.mark.parametrize("name", [
    "sudo", "elasticsearch", "elasticsearch-exporter"
])
def test_packages(host, name):
    pkg = host.package(name)
    assert host.system_info.distribution == 'ubuntu'  
    assert pkg.is_installed is True

@pytest.mark.parametrize(("dir","usr","grp"), [ \
("/etc/elasticsearch", "root","elasticsearch")
])
def test_confdirs(host, dir, usr, grp):
    d = host.file(dir)
    assert d.exists
    assert d.is_directory is True
    assert d.user  == usr
    assert d.group == grp
    assert d.mode  == 0o2750

@pytest.mark.parametrize(("file","usr","grp"), [ \
("/etc/elasticsearch/elasticsearch.yml", "elasticsearch","elasticsearch")
])
def test_conffiles(host, file, usr, grp):
    f = host.file(file)
    assert f.exists
    assert f.user == usr
    assert f.group == grp
    assert f.mode == 0o644

@pytest.mark.parametrize(("path","usr","grp"), [ \
("/data", "elasticsearch","elasticsearch")
])
def test_data_dir(host, path, usr, grp):
    p = host.file(path)
    assert p.exists is True
    assert p.is_directory is True
    assert p.user == usr
    assert p.group == grp
    assert p.mode == 0o755


@pytest.mark.parametrize(("dir","usr","grp"), [ \
("/var/log/elasticsearch/", "elasticsearch","elasticsearch"),\
])
def test_log_dirs(host, dir, usr, grp):
    d = host.file(dir)
    assert d.exists
    assert d.is_directory is True
    assert d.user  == usr
    assert d.group == grp
    assert d.mode  == 0o750
