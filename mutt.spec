Summary:	The Mutt Mail User Agent
Summary(de):	Der Mutt Mail-User-Agent 
Summary(fr):	Agent courrier Mutt
Summary(pl):	Program pocztowy Mutt
Summary(tr):	Mutt elektronik posta programý
Name:		mutt
Version:	1.2.5i
Release:	5
Epoch:		4
License:	GPL
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Source0:	ftp://ftp.mutt.org/pub/mutt/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	patches_sec.txt
Source3:	patches_bj.txt
Source4:	%{name}.png
#Patch0:	%{name}-mail.patch
#Patch1:	%{name}-confdir.patch
Patch2:		http://www.spinnaker.de/mutt/patch-1.2.rr.compressed.1.gz
# Part of that patches I changed by hand to fit them into newer version
# (bonkey)
Patch3:		patch-0.00.sec+bonk.patchlist.1
Patch4:		%{name}-blanklines.patch
Patch7:		http://sec.42.org/mutt/patch-0.94.7.sec.previous_jump.1
Patch9:		http://sec.42.org/mutt/patch-0.94.7.vikas.word_chars.1
Patch10:	http://sec.42.org/mutt/patch-0.95.3.bj.ed_mtime.1
Patch12:	http://sec.42.org/mutt/patch-0.95.4.bj.status-time.1
Patch14:	http://sec.42.org/mutt/patch-0.95.4.sec.keypad.1
Patch16:	http://sec.42.org/mutt/patch-0.95.4.sec.reverse_reply.1
Patch17:	http://sec.42.org/mutt/patch-0.95.4.vikas.print_index.1
Patch18:	http://sec.42.org/mutt/patch-0.95.6.as.mark-old.1
Patch19:	http://sec.42.org/mutt/patch-0.95.bj.hash_destroy.2
Patch20:	http://sec.42.org/mutt/patch-0.95.sec.condense_pgp.1
Patch22:	http://sec.42.org/mutt/patch-1.02.sec._A.1
#Patch23:	http://www.murkworks.to/blank-line.patch
#Patch24:	http://www.albedo.art.pl/~kbryd/mutt/%{name}_package.tar.gz
Patch25:	%{name}-dot-lock.patch
Patch26:	%{name}-pl.po.patch
Patch27:	%{name}-nosetgid.patch
Patch28:	%{name}-md5.patch
Patch29:	%{name}-imap.patch
URL:		http://www.mutt.org/
Requires:	smtpdaemon
Requires:	mailcap
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Mutt is a small but very poweful full-screen Unix mail client.
Features include MIME support, color, POP3 support, message threading,
bindable keys, and threaded sorting mode.

%description -l de
Mutt ist ein kleiner aber leistungsfähiger Vollbild-Mail-Client für
Unix mit MIME-Unterstützung, Farbe, POP3-Unterstützung,
Nachrichten-Threading, zuweisbaren Tasten und Sortieren nach Threads.

%description -l fr
mutt est un client courrier Unix plein écran, petit mais très
puissant. Il dispose de la gestion MIME, des couleurs, de la gestion
POP, des fils de discussion, des touches liées et d'un mode de tri sur
les fils.

%description -l pl
Mutt jest niewielkim programem pocztowym dla terminali tekstowych
posiadaj±cym du¿e mo¿liwo¶ci. Obs³uguje MIME, POP3, cztery formaty
skrzynek pocztowych, kolory, w±tki, ocenê wa¿no¶ci listów (scoring)
oraz skompresowane foldery.

%description -l tr
Mutt, küçük ama çok güçlü bir tam-ekran Unix mektup istemcisidir. MIME
desteði, renk ve POP3 desteði içerir.

%prep
%setup -q -n %{name}-%(echo %{version} | sed 's/i$//')
#%patch0 -p0
#%patch1 -p1 
%patch2 -p1 
%patch3 -p1
%patch4 -p1
%patch7 -p1
%patch9 -p0
%patch10 -p0
%patch12 -p1
%patch14 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p0
%patch20 -p1
%patch22 -p1
#%patch23 -p0
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1

%build
mv -f aclocal.m4 acinclude.m4
aclocal
automake
autoconf
CFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS} -fno-strict-aliasing"
%configure \
	--with-sharedir=%{_datadir} \
	--enable-pop \
	--enable-imap \
	--with-curses \
	--disable-warnings \
	--disable-domain \
        --enable-compressed \
	--with-mailpath=/var/mail \
	--with-homespool=Mailbox \
	--with-ssl \
	--with-charmaps \
	--with-docdir=%{_defaultdocdir}/%{name}-%{version} \
	--enable-external-dotlock \
	--enable-locales-fix

%{__make} keymap.h
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Mail,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

install %{SOURCE2} %{SOURCE3} .

gzip -9nf contrib/{*rc*,*cap*} \
	ChangeLog README TODO NEWS README.SECURITY README.SSL README.UPGRADE \
	patches_{bj,sec}.txt

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz contrib/{*rc*,*cap*} doc/manual*html
%config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/Muttrc
%attr(755,root,root) %{_bindir}/mutt
%attr(755,root,root) %{_bindir}/pgpewrap
%attr(755,root,root) %{_bindir}/pgpring
%attr(755,root,root) %{_bindir}/mutt_dotlock

%{_applnkdir}/Network/Mail/mutt.desktop
%{_pixmapsdir}/mutt.png
%{_mandir}/man*/*
