Summary:	The Mutt Mail User Agent
Summary(de):	Der Mutt Mail-User-Agent 
Summary(fr):	Agent courrier Mutt
Summary(pl):	Program pocztowy Mutt
Summary(tr):	Mutt elektronik posta programý
Name:		mutt
Version:	0.95.4
Release:	1i
Copyright:	GPL
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Source0:	ftp://riemann.iam.uni-bonn.de/pub/mutt/%{name}-%{version}i.tar.gz
Source1:	mutt.wmconfig
Source2:	Muttrc
Source3:	mutt.pl.po
Patch:		mutt-mail.patch
URL:		http://www.mutt.org/
Requires:	smtpdaemon
Requires:	mailcap
Buildroot:	/tmp/%{name}-%{version}-root

%description
Mutt is a small but very poweful full-screen Unix mail client.
Features include MIME support, color, POP3 support, message threading,
bindable keys, and threaded sorting mode.

%description -l de
Mutt ist ein kleiner aber leistungsfähiger Vollbild-Mail-Client für Unix mit
MIME-Unterstützung, Farbe, POP3-Unterstützung, Nachrichten-Threading,
zuweisbaren Tasten und Sortieren nach Threads.

%description -l pl
Mutt jest niewielkim programem pocztowym dla terminali tekstowych
posiadaj±cym du¿e mo¿liwo¶ci. Obs³uguje MIME, POP3, cztery formaty
skrzynek pocztowych, obs³uguje kolory, w±tki i ocenê wa¿no¶ci listów
(scoring).  W tej wersji dodano tak¿e obs³ugê skompresowanych folderów.

%description -l fr
mutt est un client courrier Unix plein écran, petit mais très puissant.
Il dispose de la gestion MIME, des couleurs, de la gestion POP, des fils
de discussion, des touches liées et d'un mode de tri sur les fils.

%description -l tr
Mutt, küçük ama çok güçlü bir tam-ekran Unix mektup istemcisidir. MIME desteði,
renk ve POP3 desteði içerir.

%prep
%setup -q 
%patch -p0

install %{SOURCE3} $RPM_BUILD_DIR/%{name}-%{version}/po/pl.po

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s \
        ./configure \
	--prefix=/usr \
	--with-sharedir=/usr/share \
	--sysconfdir=/etc \
	--enable-pop \
	--enable-imap \
	--with-curses \
	--disable-warnings \
	--disable-domain \
        --enable-compressed \
	--with-docdir=/usr/doc/mutt-%{version}

make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

#make prefix=$RPM_BUILD_ROOT/usr sharedir=$RPM_BUILD_ROOT/etc install
make install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/mutt
install %{SOURCE2} $RPM_BUILD_ROOT/etc/Muttrc

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/* \
	contrib/{*rc,*cap} \
	$RPM_BUILD_ROOT/usr/doc/mutt-%{version}/{*.txt,ChangeLog,README,TODO,NEWS,README.SECURITY}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc /usr/doc/%{name}-%{version}/*.gz

%config(noreplace) %verify(not size md5 mtime) /etc/Muttrc
%config(missingok) /etc/X11/wmconfig/mutt

%attr(0755,root,root) /usr/bin/mutt
%attr(2755,root,mail) /usr/bin/mutt_dotlock

%lang(en) /usr/man/man1/*
/usr/share/charsets

%lang(en) /usr/share/locale/de/LC_MESSAGES/mutt.mo
%lang(es) /usr/share/locale/es/LC_MESSAGES/mutt.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/mutt.mo
%lang(it) /usr/share/locale/it/LC_MESSAGES/mutt.mo
%lang(pl) /usr/share/locale/pl/LC_MESSAGES/mutt.mo
%lang(ru) /usr/share/locale/ru/LC_MESSAGES/mutt.mo
%lang(uk) /usr/share/locale/uk/LC_MESSAGES/mutt.mo

%changelog
* Thu Mar 25 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.95.4-1i]
- rewrited %install (now we use DESTDIR style install),
- added --sysconfdir=/etc adnd changed --with-sharedir to /usr/share,
- added Requires: mailcap (mutt use /etc/mime.types).
- added /usr/share/charsets in %files.

* Thu Mar 25 1999 Artur Frysiak <wiget@pld.org.pl>
- upgraded to 0.95.4i
- linked with ncurses
- removed man group from man pages
- updated pl.po (sync with i18n CVS)

* Sat Feb 13 1999 Micha³ Kuratczyk <kura@wroclaw.art.pl>
  [0.95.3i-3d]
- upgraded to 0.95.3i

* Thu Feb 10 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [0.95i-3d]
- added gzipping documentation
- simplification in %files
- cosmetic changes

* Mon Dec 14 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [0.95i-1]
- remove patch for compressed folders (not available yet)
- added %%lang macros
- added some missing doc files
- locale files included

* Sat Sep 19 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [0.93.2i-1d]
- added pl translation,
- added patch for compressed folders,
- rewrites system Muttrc based on ones from Roland Rosenfeld.

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
