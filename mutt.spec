Summary:     The Mutt Mail User Agent
Summary(de): Der Mutt Mail-User-Agent 
Summary(fr): Agent courrier Mutt
Summary(tr): Mutt elektronik posta programý
Name:        mutt
Version:     0.93.2i
Release:     2
Copyright:   GPL
Group:       Applications/Mail
Source:      ftp://riemann.iam.uni-bonn.de/pub/mutt/%{name}-%{version}.tar.gz
Source1:     mutt.wmconfig
URL:         http://www.mutt.org/
Requires:    smtpdaemon, mailcap, pgp
Buildroot:   /tmp/%{name}-%{version}-root

%description
Mutt is a small but very poweful full-screen Unix mail client.
Features include MIME support, color, POP3 support, message threading,
bindable keys, and threaded sorting mode.

%description -l de
Mutt ist ein kleiner aber leistungsfähiger Vollbild-Mail-Client für Unix mit
MIME-Unterstützung, Farbe, POP3-Unterstützung, Nachrichten-Threading,
zuweisbaren Tasten und Sortieren nach Threads.

%description -l fr
mutt est un client courrier Unix plein écran, petit mais très puissant.
Il dispose de la gestion MIME, des couleurs, de la gestion POP, des fils
de discussion, des touches liées et d'un mode de tri sur les fils.

%description -l tr
Mutt, küçük ama çok güçlü bir tam-ekran Unix mektup istemcisidir. MIME desteði,
renk ve POP3 desteði içerir.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/slang" LDFLAGS=-s \
./configure \
	--prefix=/usr \
	--with-sharedir=/etc \
	--enable-pop \
	--with-slang \
	--disable-warnings \
	--disable-domain \
	--with-docdir=$RPM_BUILD_DIR/mutt-%{version}/rpm_docs
make
#make manual.txt -C doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make prefix=$RPM_BUILD_ROOT/usr sharedir=$RPM_BUILD_ROOT/etc install

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/mutt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc Mush.rc Pine.rc README sample.* NEWS doc/manual.txt rpm_docs
%config /etc/Muttrc
/etc/X11/wmconfig/mutt
%attr(2755, root, mail) /usr/bin/mutt
%attr(0755, root,  man) /usr/man/man1/mutt.1

%changelog
* Sun Sep  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.93.2i-1]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added using %{SOURCE#} macro in %install,
- changed base Source Url to ftp://riemann.iam.uni-bonn.de/pub/mutt/.

* Wed Jul 29 1998 Bill Nottingham <notting@redhat.com>
- fix setgid removal
- spec file comsetics

* Tue Jul 28 1998 Jeff Johnson <jbj@redhat.com>
- security fix
- turn off setgid mail.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 0.91.1

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to mutt-0.89.1

* Thu Oct 16 1997 Otto Hammersmith <otto@redhat.com>
- Updated to mutt 0.85.
- added wmconfig entries.
- removed mime.types

* Mon Sep 1 1997 Donnie Barnes <djb@redhat.com>
- Rebuilt to insure all sources were fresh and patches were clean.

* Wed Aug 6 1997 Manoj Kasichainula <manojk@io.com>
 - Initial version for 0.81(e)
