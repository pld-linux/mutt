Summary:	The Mutt Mail User Agent
Summary(de):	Der Mutt Mail-User-Agent 
Summary(fr):	Agent courrier Mutt
Summary(pl):	Program pocztowy Mutt
Summary(tr):	Mutt elektronik posta programý
Name:		mutt
Version:	0.96.2
Release:	1i
Copyright:	GPL
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Source0:	ftp://riemann.iam.uni-bonn.de/pub/mutt/%{name}-%{version}i.tar.gz
Source1:	mutt.wmconfig
Source2:	Muttrc
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

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr \
	--with-sharedir=%{_datadir} \
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

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	contrib/{*rc,*cap} \
	$RPM_BUILD_ROOT/usr/doc/mutt-%{version}/{*.txt,ChangeLog,README,TODO,NEWS,README.SECURITY}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc /usr/doc/%{name}-%{version}/*.gz

%config(noreplace) %verify(not size md5 mtime) /etc/Muttrc
%config(missingok) /etc/X11/wmconfig/mutt

%attr(0755,root,root) %{_bindir}/mutt
%attr(2755,root,mail) %{_bindir}/mutt_dotlock

%lang(en) %{_mandir}/man1/*
%{_datadir}/charsets
