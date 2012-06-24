Summary:	A list monitor with a visual output
Summary(de):	Face Saver Datenbank-Tools
Summary(fr):	Outils pour la base de donn�es de sauvegarde des aspects
Summary(pl):	Program do wizualnego monitorowania listy
Summary(tr):	Y�z (face) sunucusu veri taban� ara�lar�
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

%description -l de
Das faces-Paket ist vor allem f�r exmh gedacht. Sie k�nnen ein
beliebiges Foto in ein 'face' verwandeln, das dann per E-Mail
�bertragen wird und von exmh und anderen Mail-Programmen erscheint.

%description -l fr
Le package faces est principalement utilis� avec exmh. Vous pouvez
prendre une photo de quelque chose et le transformer en une ``face''
qui peut �tre transmise dans tous les courriers �lctroniques et sera
visible dans exmh et les autres mailers.

%description -l pl
faces jest programem s�u��cym do wizualnego monitorowania listy
(zazwyczaj jest to lista nadchodz�cych wiadomo�ci, lista zada� w
kolejce drukowania czy lista u�ytkownik�w systemu). Faces dzia�a w
kilku r�nych trybach: nadzoruj�c nadchodz�c� poczt�, nadzoruj�c ca�y
plik pocztowy, nadzoruj�c podan� kolejk� drukowania, nadzoruj�c
u�ytkownik�w na danym komputerze oraz wykonuj�c inne, wyszczeg�lnione
czynno�ci nadzoruj�ce. Pakiet faces zawiera r�wnie� narz�dzie s�u��ce
do do��czania (zeskanowanego, skompresowanego) wizerunku twarzy w
wiadomo�ciach pocztowych. Obrazek ten powinien by� skompresowany w
szczeg�lny spos�b, dzi�ki czemu b�dzie m�g� zosta� zdekompresowany i
wy�wietlony w locie przez program pocztowy. Ta funkcja jest zazwyczaj
wykorzystywana w systemie obs�ugi poczty exmh.

Nale�y zainstalowa� faces je�li pragnie si� wykorzysta� zdolno��
nadzorowania list b�d�c� cech� tego pakietu. Je�li chce si� do��cza�
wizerunki twarzy w wiadomo�ciach poczty elektronicznej, trzeba b�dzie
r�wnie� zainstalowa� pakiet faces-xface. Je�li pragnie si� pisa�
aplikacje dla xface, nale�y dodatkowo zainstalowa� pakiet faces-devel.

%description -l tr
Faces paketi daha �ok exmh yaz�l�m� ile kullan�lmak i�in
haz�rlanm��t�r. Herhangi bir g�r�nt�y� bir 'y�z'e �evirebilir ve bunu
mektuplara ekleyerek exmh ve benzeri yaz�l�mlar kullanan mektup okuma
yaz�l�mlar�nda belirmesini sa�layabilirsiniz.

%package xface
Summary:	Utilities needed by mailers for handling Faces' X-face images
Summary(de):	Utilities zur Behandlung von X-Face-Headers
Summary(fr):	Utilitaires pour g�rer les en-t�tes X-Face
Summary(pl):	Narz�dzia potrzebne programom pocztowym do obs�ugi nag��wk�w X-Face
Summary(tr):	X-Face ba�l�klar�n� i�leme ara�lar�
Group:		Applications/Mail
Requires:	netpbm-progs

%description xface
Faces-xface includes the utilities that mail user agent programs need
to handle X-Face mail headers. When an email program reads the X-face
header line in an email message, it calls these utilities to display
the face image included in the message.

%description xface -l de
Dies sind Dienstprogramme zum Verarbeiten von X-Face-Mail-Headern. Sie
werden von Mail-Programmen aufgerufen, um ein 'Face' einer Nachricht
darzustellen.

%description xface -l fr
Ce sont des utilitaires pour prendre en charge des en-t�te de mail X.
il sont appel�s par les lecteurs de mail pour affciher ces parties de
message.

%description xface -l pl
Pakiet faces-xface zawiera narz�dzia potrzebne programom pocztowym do
wy�wietlania obrazk�w zawartych w nag��wkach X-Face. Kiedy program
pocztowy czyta z nag��wka lini� X-Face, uruchamia te narz�dzia �eby
wy�wietli� obrazek zawarty w nag��wku.

%description xface -l tr
Bu paket. X-Face mektup ba�l�klar�n� i�leyen ara�lar� i�erir. Bu
ara�lar�, bir mesajdaki bir y�z� g�r�nt�lemek isteyen e-posta
okuyucular� kullan�r.

%package devel
Summary:	The Faces program's library and header files
Summary(de):	Face-Saver-Library und Header
Summary(fr):	Biblioth�que et en-t�te Face saver
Summary(pl):	Biblioteka statyczna i plik nag��wkowy faces
Summary(tr):	Face sunucu kitapl��� ve ba�l�klar�
Group:		Development/Libraries

%description devel
Faces-devel contains the faces program development environment, (i.e.,
the static libraries and header files).

%description devel -l de
Dies ist die xface-Entwicklungsumgebung. Sie enth�lt die statischen
Libraries und die Header-Dateien f�r xface-Entwicklungsarbeiten.

%description devel -l fr
Environnement de d�veloppement xface. Contient les biblioth�ques et
fichiers en-t�tes pour faire du d�veloppement xface.

%description devel -l pl
Pakiet zawiera plik nag��wkowy oraz bibliotek� statyczn�.

%description devel -l tr
Bu paket, xface geli�tirme ortam�n� sunar. Gerekli statik kitapl�klar�
ve ba�l�k dosyalar�n� i�erir.

%prep
%setup -q -n faces
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
%{_mandir}/man1/uncompface.1.*
%{_mandir}/man3/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/compface.h
%{_libdir}/libcompface.a
