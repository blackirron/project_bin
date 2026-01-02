import os
import ctypes

CLONE_NEWUTS  = 0x04000000
CLONE_NEWPID  = 0x20000000
CLONE_NEWNS   = 0x00020000

libc = ctypes.CDLL("libc.so.6")

def setup_namespaces():
    libc.unshare(CLONE_NEWUTS | CLONE_NEWPID | CLONE_NEWNS)
    os.sethostname(b"mycontainer")
