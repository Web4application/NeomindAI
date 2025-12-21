import sys

def options(opt):
        opt.load('compiler_c')

def configure(conf):
        conf.load('compiler_c')
        conf.env.INCLUDES_TEST      = ['/usr/include'] 1

        if sys.platform != 'win32': 2
                conf.env.DEFINES_TEST   = ['TEST']
                conf.env.CFLAGS_TEST    = ['-O0'] 3
                conf.env.LIB_TEST       = ['m']
                conf.env.LIBPATH_TEST   = ['/usr/lib']
                conf.env.LINKFLAGS_TEST = ['-g']
                conf.env.INCLUDES_TEST  = ['/opt/gnome/include']

def build(bld):
        mylib = bld.stlib(
                source   = 'test_staticlib.c',
                target   = 'teststaticlib',
                use      = 'TEST') 4

        if mylib.env.CC_NAME == 'gcc':
                mylib.cxxflags = ['-O2'] 5
