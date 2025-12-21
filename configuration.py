# using /home/waf/bin/waf configure
#

---
Setting top to
/disk/comp/waf/docs/book/examples/cprog_pkgconfig
---
Setting out to
/disk/comp/waf/docs/book/examples/cprog_pkgconfig/build
---
Checking for program pkg-config
/usr/bin/pkg-config
find program=['pkg-config'] paths=['/usr/local/bin', '/usr/bin'] var='PKGCONFIG' -> '/usr/bin/pkg-config'
---
Checking for pkg-config version >= 0.0.0
['/usr/bin/pkg-config', '--atleast-pkgconfig-version=0.0.0']
yes
['/usr/bin/pkg-config', '--modversion', 'pango']
out: 1.28.0

---
Checking for pango
['/usr/bin/pkg-config', 'pango']
yes
---
Checking for pango
['/usr/bin/pkg-config', 'pango']
yes
---
Checking for pango 0.1.0
['/usr/bin/pkg-config', 'pango >= 0.1.0', 'pango < 9.9.9', '--cflags', '--libs', 'pango']
out: -pthread -I/usr/include/pango-1.0 -I/usr/include/glib-2.0 -I/usr/lib64/glib-2.0/include
     -pthread -lpango-1.0 -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lrt -lglib-2.0

yes
---
Checking for sdl-config
['sdl-config', '--cflags', '--libs']
out: -I/usr/include/SDL -D_GNU_SOURCE=1 -D_REENTRANT
-L/usr/lib64 -lSDL -lpthread

yes
---
Checking for mpicc
['mpicc', '--showme:compile', '--showme:link']
out: -pthread libtool: link: -pthread -L/usr/lib64 -llammpio -llamf77mpi -lmpi -llam -lutil -ldl
