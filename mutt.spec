#
# Conditional build:
%bcond_with slang		# use slang library instead of ncurses
%bcond_with nntp		# use VVV's NNTP patch
%bcond_with esmtp		# use esmtp patch
%bcond_without sasl		# don't use sasl
%bcond_without home_etc		# don't use home_etc
#
Summary:	The Mutt Mail User Agent
Summary(de):	Der Mutt Mail-User-Agent
Summary(es):	Mutt, cliente de correo electrСnico
Summary(fr):	Agent courrier Mutt
Summary(ko):	еь╫╨ф╝ ╠Б╧щюг MUA
Summary(pl):	Program pocztowy Mutt
Summary(pt_BR):	Mutt, cliente de correio eletrТnico
Summary(ru):	Почтовая клиентская программа Mutt
Summary(tr):	Mutt elektronik posta programЩ
Summary(uk):	Поштова кл╕╓нтська програма Mutt
Name:		mutt
Version:	1.4.2.1
Release:	4
Epoch:		6
License:	GPL
Group:		Applications/Mail
Source0:	ftp://ftp.mutt.org/mutt/%{name}-%{version}i.tar.gz
# Source0-md5:	710bd56d3c4c4bcd1403bc4e053f7476
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}.1.pl
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
Patch14:	%{name}-pgp_hook.patch
Patch15:	%{name}-manual.patch
Patch16:	%{name}-send_charset.patch
Patch17:	%{name}-xface.patch
Patch18:	%{name}-sasl2.patch
Patch19:	%{name}-nntp.patch
Patch20:	%{name}-esmtp.patch
Patch21:	%{name}-home_etc.patch
Patch22:	%{name}-kill_warnings.patch
URL:		http://www.mutt.org/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_sasl:BuildRequires:	cyrus-sasl-devel >= 2.1.0}
%{?with_home_etc:BuildRequires:	home-etc-devel >= 1.0.8}
BuildRequires:	gettext-devel
%{!?with_slang:BuildRequires:	ncurses-devel >= 5.0}
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	sgml-tools
BuildRequires:	sgml-tools-dtd
%{?with_slang:BuildRequires:	slang-devel}
%{?with_esmtp:BuildRequires:	libesmtp-devel}
Requires:	iconv
Requires:	mailcap
%{?with_home_etc:Requires:	home-etc >= 1.0.8}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	"-fomit-frame-pointer"

%description
Mutt is a small but very poweful full-screen Unix mail client.
Features include MIME support, color, POP3 support, message threading,
bindable keys, and threaded sorting mode.

%description -l de
Mutt ist ein kleiner aber leistungsfДhiger Vollbild-Mail-Client fЭr
Unix mit MIME-UnterstЭtzung, Farbe, POP3-UnterstЭtzung,
Nachrichten-Threading, zuweisbaren Tasten und Sortieren nach Threads.

%description -l es
Mutt es un pequeЯo, pero muy potente cliente de correo en pantalla
llena. Incluye soporte a tipos MINE, color, POP3; encadenamiento de
mensajes, teclas configurables y clasificaciones por encadenamiento.

%description -l fr
mutt est un client courrier Unix plein Иcran, petit mais trХs
puissant. Il dispose de la gestion MIME, des couleurs, de la gestion
POP, des fils de discussion, des touches liИes et d'un mode de tri sur
les fils.

%description -l ko
Mutt╢б юшаЖ╦╦ ╦е©Л ╟╜╥бгя еь╫╨ф╝ ╠Б╧щюг ╦чюо е╛╤Сюл╬Пф╝юл╢ы. Mutt╢б
╦╧ю╨ ╪Ёа╓юл ╟║╢иго╢ы. ╠в╦╝╟М, е╟╧ыюн╣Ы, е╟╨╦╣Е ╦че╘╥н, ╦чюо ╫╨╥╧╣Ы╟З
╟╟ю╨ аЬ╨╦╣х гЭеб©м а╓╠тг╔гЖ╫д ╟к╩Ж, ╦чюо©║╪╜ ╪╠ец╣х ╠в╥Люг Ё╩©К©║╪╜
╟╜╥бго╟т юоа╓гя фпеою╩ цё╬фЁ╩╢б ╟мю╩ аЖ©Ьгтю╦╥н╫А ╦чюоюг фд©Ж ю╞юЗ©║╟т
╟║юЕ юШгуго╢ы.

%description -l pl
Mutt jest niewielkim programem pocztowym dla terminali tekstowych,
posiadaj╠cym du©e mo©liwo╤ci. ObsЁuguje MIME, POP3, cztery formaty
skrzynek pocztowych, kolory, w╠tki, ocenЙ wa©no╤ci listСw (scoring)
oraz skompresowane foldery.

%description -l pt_BR
O Mutt И um pequeno mas muito poderoso cliente de correio em tela
cheia. Inclui suporte a tipos MIME, cor, POP3, encadeamento de
mensagens, teclas configurАveis e classificaГЦo por encadeamento.

%description -l ru
Mutt - это небольшой, но мощный полноэкранный почтовый клиент.
Включает поддержку MIME, цвет, поддержку POP3 и IMAP, группировку
сообщений по цепочкам, переопределяемые клавиши, поддержку pgp/gpg и
сортировку сообщений в цепочках. Включает также (пока что
экспериментальную) поддержку NNTP.

%description -l tr
Mutt, kЭГЭk ama Гok gЭГlЭ bir tam-ekran Unix mektup istemcisidir. MIME
desteПi, renk ve POP3 desteПi iГerir.

%description -l uk
Mutt - це невеликий, але потужний повноекранний поштовий кл╕╓нт.
М╕стить п╕дтримку MIME, кол╕р, п╕дтримку POP3 та IMAP, групування
пов╕домлень по ланцюжкам, перевизначення клав╕ш, п╕дтримку pgp/gpg та
сортування пов╕домлень у ланцюжках. М╕стить також (поки що
експериментальну) п╕дтримку NNTP.

%prep
%setup -q -n %{name}-%(echo %{version} | sed 's/i$//')
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
#%patch13 -p0
%patch14 -p1
%patch16 -p1
%patch17 -p1
%{?with_sasl:%patch18 -p1}
%{?with_nntp:%patch19 -p1}
%{?with_esmtp:%patch20 -p1}
%{?with_home_etc:%patch21 -p1}
%patch22 -p1

# force regeneration (manual.sgml is modified by some patches)
rm -f doc/{manual*.html,manual.txt}

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	%{!?debug:--disable-debug} %{?debug:--enable-debug} \
	%{!?with_slang:--with-curses} \
	%{?with_slang:--with-slang} \
	--enable-compressed \
	--enable-external-dotlock \
	--enable-imap \
	--without-included-gettext \
	--enable-mailtool \
	--with-mixmaster \
	--enable-pop \
	%{?with_nntp:--enable-nntp} \
	--with-regex \
	%{?with_sasl:--with-sasl} %{!?with_sasl:--without-sasl} \
	%{?with_home_etc:--with-home-etc} %{!?with_home_etc:--without-home-etc} \
	%{?with_esmtp:--enable-libesmtp --with-libesmtp=/usr} \
	--with-ssl \
	--disable-warnings \
	--with-docdir=%{_datadir}/%{name} \
	--with-homespool=Maildir \
	--with-mailpath=/var/mail \
	--with-sharedir=%{_datadir} \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--datadir=%{_datadir} \
	--mandir=%{_mandir} \
	--sysconfdir=%{_sysconfdir}

%{__make}
%{__make} manual.txt -C doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_mandir}/pl/man1,%{_datadir}/%{name}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__patch} -p0 -d $RPM_BUILD_ROOT%{_sysconfdir} < %PATCH16

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/pl/man1
install doc/manual.txt $RPM_BUILD_ROOT%{_datadir}/%{name}

# conflict with qmail
rm -f $RPM_BUILD_ROOT%{_mandir}/man5/mbox.5*

rm -f $RPM_BUILD_ROOT/etc/mime.types

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc contrib/{*rc*,*cap*} ChangeLog README TODO NEWS README.SECURITY README.SSL README.xface %{?with_esmtp: Muttrc.esmtp}
%config(noreplace,missingok) %verify(not md5 size mtime) %{_sysconfdir}/Muttrc
%attr(755,root,root) %{_bindir}/mutt
%attr(755,root,root) %{_bindir}/flea
%attr(755,root,root) %{_bindir}/muttbug
%attr(755,root,root) %{_bindir}/pgp*
%attr(2755,root,mail) %{_bindir}/mutt_dotlock

%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/mutt.png
%{_mandir}/man*/*
%lang(pl) %{_mandir}/pl/man*/*
