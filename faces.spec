# TODO
# - devel collides with compface-devel
Summary:	A list monitor with a visual output
Summary(de.UTF-8):   Face Saver Datenbank-Tools
Summary(fr.UTF-8):   Outils pour la base de données de sauvegarde des aspects
Summary(pl.UTF-8):   Program do wizualnego monitorowania listy
Summary(tr.UTF-8):   Yüz (face) sunucusu veri tabanı araçları
Name:		faces
Version:	1.6.1
Release:	20
License:	Freeware
Group:		Applications/Mail
# this file differs from the one from CVS
#Source0:	ftp://ftp.cs.indiana.edu/pub/faces/faces/%{name}-%{version}.tar.Z
Source0:	%{name}-%{version}.tar.Z
# Source0-md5:	73b1ba54e57bf99f85d3ccf7be95c17d
Patch0:		%{name}-make.patch
Patch1:		%{name}-awk.patch
Patch2:		%{name}-string.patch
Patch3:		%{name}-fix.patch
Patch4:		%{name}-error.patch
BuildRequires:	XFree86-devel
BuildRequires:	bison
Requires:	netpbm-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Faces is a program for visually monitoring a list (typically a list of
incoming mail messages, a list of jobs in a print queue or a list of
system users). Faces operates in five different modes: monitoring for
new mail, monitoring an entire mail file, monitoring a specified print
queue, monitoring users on a machine and custom monitoring. Faces also
includes a utility for including a face image (a compressed, scanned
image) with mail messages. The image has to be compressed in a certain
way, which can then be uncompressed and displayed on-the-fly in the
mail program. This feature of faces is typically used with the exmh
mail handling system.

Install faces if you'd like to use its list monitoring capability or
its face image inclusion capability. If you would like to include face
images in email, you'll also need to install the faces-xface package.
If you would like to develop xface applications, you'll need to also
install faces-devel.

%description -l de.UTF-8
Das faces-Paket ist vor allem für exmh gedacht. Sie können ein
beliebiges Foto in ein 'face' verwandeln, das dann per E-Mail
übertragen wird und von exmh und anderen Mail-Programmen erscheint.

%description -l fr.UTF-8
Le package faces est principalement utilisé avec exmh. Vous pouvez
prendre une photo de quelque chose et le transformer en une ``face''
qui peut être transmise dans tous les courriers élctroniques et sera
visible dans exmh et les autres mailers.

%description -l pl.UTF-8
faces jest programem służącym do wizualnego monitorowania listy
(zazwyczaj jest to lista nadchodzących wiadomości, lista zadań w
kolejce drukowania czy lista użytkowników systemu). Faces działa w
kilku różnych trybach: nadzorując nadchodzącą pocztę, nadzorując cały
plik pocztowy, nadzorując podaną kolejkę drukowania, nadzorując
użytkowników na danym komputerze oraz wykonując inne, wyszczególnione
czynności nadzorujące. Pakiet faces zawiera również narzędzie służące
do dołączania (zeskanowanego, skompresowanego) wizerunku twarzy w
wiadomościach pocztowych. Obrazek ten powinien być skompresowany w
szczególny sposób, dzięki czemu będzie mógł zostać zdekompresowany i
wyświetlony w locie przez program pocztowy. Ta funkcja jest zazwyczaj
wykorzystywana w systemie obsługi poczty exmh.

Należy zainstalować faces jeśli pragnie się wykorzystać zdolność
nadzorowania list będącą cechą tego pakietu. Jeśli chce się dołączać
wizerunki twarzy w wiadomościach poczty elektronicznej, trzeba będzie
również zainstalować pakiet faces-xface. Jeśli pragnie się pisać
aplikacje dla xface, należy dodatkowo zainstalować pakiet faces-devel.

%description -l tr.UTF-8
Faces paketi daha çok exmh yazılımı ile kullanılmak için
hazırlanmıştır. Herhangi bir görüntüyü bir 'yüz'e çevirebilir ve bunu
mektuplara ekleyerek exmh ve benzeri yazılımlar kullanan mektup okuma
yazılımlarında belirmesini sağlayabilirsiniz.

%package xface
Summary:	Utilities needed by mailers for handling Faces' X-face images
Summary(de.UTF-8):   Utilities zur Behandlung von X-Face-Headers
Summary(fr.UTF-8):   Utilitaires pour gérer les en-têtes X-Face
Summary(pl.UTF-8):   Narzędzia potrzebne programom pocztowym do obsługi nagłówków X-Face
Summary(tr.UTF-8):   X-Face başlıklarını işleme araçları
Group:		Applications/Mail
Requires:	netpbm-progs

%description xface
Faces-xface includes the utilities that mail user agent programs need
to handle X-Face mail headers. When an email program reads the X-face
header line in an email message, it calls these utilities to display
the face image included in the message.

%description xface -l de.UTF-8
Dies sind Dienstprogramme zum Verarbeiten von X-Face-Mail-Headern. Sie
werden von Mail-Programmen aufgerufen, um ein 'Face' einer Nachricht
darzustellen.

%description xface -l fr.UTF-8
Ce sont des utilitaires pour prendre en charge des en-tête de mail X.
il sont appelés par les lecteurs de mail pour affciher ces parties de
message.

%description xface -l pl.UTF-8
Pakiet faces-xface zawiera narzędzia potrzebne programom pocztowym do
wyświetlania obrazków zawartych w nagłówkach X-Face. Kiedy program
pocztowy czyta z nagłówka linię X-Face, uruchamia te narzędzia żeby
wyświetlić obrazek zawarty w nagłówku.

%description xface -l tr.UTF-8
Bu paket. X-Face mektup başlıklarını işleyen araçları içerir. Bu
araçları, bir mesajdaki bir yüzü görüntülemek isteyen e-posta
okuyucuları kullanır.

%package devel
Summary:	The Faces program's library and header files
Summary(de.UTF-8):   Face-Saver-Library und Header
Summary(fr.UTF-8):   Bibliothèque et en-tête Face saver
Summary(pl.UTF-8):   Biblioteka statyczna i plik nagłówkowy faces
Summary(tr.UTF-8):   Face sunucu kitaplığı ve başlıkları
Group:		Development/Libraries

%description devel
Faces-devel contains the faces program development environment, (i.e.,
the static libraries and header files).

%description devel -l de.UTF-8
Dies ist die xface-Entwicklungsumgebung. Sie enthält die statischen
Libraries und die Header-Dateien für xface-Entwicklungsarbeiten.

%description devel -l fr.UTF-8
Environnement de développement xface. Contient les bibliothèques et
fichiers en-têtes pour faire du développement xface.

%description devel -l pl.UTF-8
Pakiet zawiera plik nagłówkowy oraz bibliotekę statyczną.

%description devel -l tr.UTF-8
Bu paket, xface geliştirme ortamını sunar. Gerekli statik kitaplıkları
ve başlık dosyalarını içerir.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
bison address.y -o address.c

%{__make} RPM_OPT_FLAGS="%{rpmcflags} -L/usr/X11R6/%{_lib}" -f Makefile.dist x11

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir}/faces,%{_mandir}/man{1,3}}

%{__make} -f Makefile.dist \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	install

install compface/compface.h $RPM_BUILD_ROOT%{_includedir}/compface.h

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES* README TODO
%attr(755,root,root) %{_bindir}/compface
%attr(755,root,root) %{_bindir}/icon2ikon
%attr(755,root,root) %{_bindir}/ikon2icon
%attr(755,root,root) %{_bindir}/fs2ikon
%attr(755,root,root) %{_bindir}/rs2icon
%attr(755,root,root) %{_bindir}/fs2xbm
%attr(755,root,root) %{_bindir}/xbm2ikon
%attr(755,root,root) %{_bindir}/xbmcut48
%attr(755,root,root) %{_bindir}/xbmsize48
%attr(755,root,root) %{_bindir}/addxface
%attr(755,root,root) %{_bindir}/mailq.faces
%attr(755,root,root) %{_bindir}/from.faces
%attr(755,root,root) %{_bindir}/lpqall.faces
%attr(755,root,root) %{_bindir}/rotary.faces
%attr(755,root,root) %{_bindir}/facesaddr
%attr(755,root,root) %{_bindir}/facesall
%attr(755,root,root) %{_bindir}/mkfacesindex
%attr(755,root,root) %{_bindir}/newscheck.faces
%attr(755,root,root) %{_bindir}/newsfrom.faces
%attr(755,root,root) %{_bindir}/faces
%attr(755,root,root) %{_bindir}/face_update
%attr(755,root,root) %{_bindir}/faces.sendmail
%{_libdir}/faces
%{_mandir}/man1/faces.1*
%{_mandir}/man1/face_update.1*
%{_mandir}/man1/compface.1*

%files xface
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uncompface
%attr(755,root,root) %{_bindir}/ikon2xbm
%{_mandir}/man1/uncompface.1*
%{_mandir}/man3/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/compface.h
%{_libdir}/libcompface.a
