import os

ROOTFS = "./rootfs"

def setup_rootfs():
    os.chroot(ROOTFS)
    os.chdir("/")
