Summary:	The Mutt Mail User Agent
Summary(de):	Der Mutt Mail-User-Agent
Summary(es):	Mutt, cliente de correo electrónico
Summary(fr):	Agent courrier Mutt
Summary(pl):	Program pocztowy Mutt
Summary(pt_BR):	Mutt, cliente de correio eletrônico
Summary(es):	Mutt, cliente de correo electrónico
Summary(tr):	Mutt elektronik posta programý
Name:		mutt
Version:	1.3.27i
Release:	5
Epoch:		5
License:	GPL
Group:		Applications/Mail
Group(cs):	Aplikace/Po¹ta
Group(da):	Programmer/Post
Group(de):	Applikationen/Post
Group(es):	Aplicaciones/Correo Electrónico
Group(fr):	Applications/Courrier
Group(is):	Forrit/Póst
Group(it):	Applicazioni/Posta
Group(no):	Applikasjoner/Epost
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/üÌÅËÔÒÏÎÎÁÑ ÐÏÞÔÁ
Group(sl):	Programi/Po¹tna
Group(sv):	Tillämpningar/Post
Source0:	ftp://ftp.mutt.org/pub/mutt/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}.1.pl
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-forcedotlock.patch
Patch2:		%{name}-muttbug-tmp.patch
Patch3:		%{name}-rr.compressed.patch
Patch4:		%{name}-cd.edit_threads.patch
Patch5:		%{name}-bj.status-time.patch
Patch6:		%{name}-devl.narrow_tree.patch
Patch7:		%{name}-vvv.quote.gz
Patch8:		%{name}-null_name.patch
Patch9:		%{name}-cd.trash_folder.patch
Patch10:	%{name}-cd.purge_message.patch
Patch11:	%{name}-cd.signatures_menu.patch
Patch12:	%{name}-folder_columns.patch
Patch13:	%{name}-nr.tag_prefix_cond.patch
URL:		http://www.mutt.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	sgml-tools
%{!?_without_sasl:BuildRequires:	cyrus-sasl-devel}
Requires:	iconv
Requires:	mailcap
Requires:	smtpdaemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mutt is a small but very poweful full-screen Unix mail client.
Features include MIME support, color, POP3 support, message threading,
bindable keys, and threaded sorting mode.

%description -l de
Mutt ist ein kleiner aber leistungsfähiger Vollbild-Mail-Client für
Unix mit MIME-Unterstützung, Farbe, POP3-Unterstützung,
Nachrichten-Threading, zuweisbaren Tasten und Sortieren nach Threads.

%description -l es
Mutt es un pequeño, pero muy potente cliente de correo en pantalla
llena. Incluye soporte a tipos MINE, color, POP3; encadenamiento de
mensajes, teclas configurables y clasificaciones por encadenamiento.

%description -l fr
mutt est un client courrier Unix plein écran, petit mais très
puissant. Il dispose de la gestion MIME, des couleurs, de la gestion
POP, des fils de discussion, des touches liées et d'un mode de tri sur
les fils.

%description -l pl
Mutt jest niewielkim programem pocztowym dla terminali tekstowych,
posiadaj±cym du¿e mo¿liwo¶ci. Obs³uguje MIME, POP3, cztery formaty
skrzynek pocztowych, kolory, w±tki, ocenê wa¿no¶ci listów (scoring)
oraz skompresowane foldery.

%description -l pt_BR
O Mutt é um pequeno mas muito poderoso cliente de correio em tela
cheia. Inclui suporte a tipos MIME, cor, POP3, encadeamento de
mensagens, teclas configuráveis e classificação por encadeamento.

%description -l tr
Mutt, küçük ama çok güçlü bir tam-ekran Unix mektup istemcisidir. MIME
desteði, renk ve POP3 desteði içerir.

%prep
%setup -q -n %{name}-%(echo %{version} | sed 's/i$//')
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p0

%build
autoconf
#PGP=%{_bindir}/pgp PGPK=%{_bindir}/pgpk
CFLAGS="%{optflags} -I%{_includedir}/slang" \
%configure \
	--enable-pop \
	--enable-imap \
	--enable-mailtool \
	--enable-external-dotlock \
	--enable-compressed \
	%{!?debug:--disable-debug} %{?debug:--enable-debug} \
	--disable-warnings \
	--with-curses \
	--with-iconv \
	--with-regex \
	--with-ssl \
	%{!?_without_sasl:--with-sasl} %{?_without_sasl:--without-sasl} \
	--without-included-nls \
	--with-homespool=Maildir \
	--with-mixmaster \
	--with-mailpath=/var/mail \
	--with-sharedir=%{_datadir} \
	--with-docdir=%{_docdir}/%{name}-%{version} \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--sysconfdir=%{_sysconfdir} \
	--datadir=%{_datadir} \
	--mandir=%{_mandir} 

%{__make}
%{__make} manual.txt -C doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Mail,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_mandir}/pl/man1

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/pl/man1

gzip -9nf contrib/{*rc*,*cap*} \
	ChangeLog README TODO NEWS README.SECURITY README.SSL 

# conflict with qmail
rm -f $RPM_BUILD_ROOT%{_mandir}/man5/mbox.5*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz contrib/{*rc*,*cap*} doc/manual*html doc/manual.txt
%config(noreplace,missingok) %verify(not md5 size mtime) %{_sysconfdir}/Muttrc
%attr(755,root,root) %{_bindir}/mutt
%attr(755,root,root) %{_bindir}/flea
%attr(755,root,root) %{_bindir}/muttbug
%attr(755,root,root) %{_bindir}/pgp*
%attr(2755,root,mail) %{_bindir}/mutt_dotlock

%{_applnkdir}/Network/Mail/mutt.desktop
%{_pixmapsdir}/mutt.png
%{_mandir}/man*/*
%lang(pl) %{_mandir}/pl/man*/*
