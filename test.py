def test_package(Package):
  lvm2 = Package("lvm2")
  assert lvm2.is_installed
