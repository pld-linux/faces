Summary:	A list monitor with a visual output.
Name:		faces
Version:	1.6.1
Release:	17
Copyright:	freeware
Group:		Applications/Mail
Source:		ftp://ftp.cs.indiana.edu/pub/faces/faces/faces-1.6.1.tar.Z
Patch0:		faces-1.6.1-make.patch
Patch1:		faces-1.6.1-awk.patch
Patch2:		faces-1.6.1-string.patch
Patch3:		faces-1.6.1-fix.patch
Requires:	libgr-progs
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Faces is a program for visually monitoring a list (typically a list of
incoming mail messages, a list of jobs in a print queue or a list of
system users).  Faces operates in five different modes: monitoring for
new mail, monitoring an entire mail file, monitoring a specified print
queue, monitoring users on a machine and custom monitoring.  Faces also
includes a utility for including a face image (a compressed, scanned
image) with mail messages.  The image has to be compressed in a certain
way, which can then be uncompressed and displayed on-the-fly in the mail
program.  This feature of faces is typically used with the exmh mail
handling system.

Install faces if you'd like to use its list monitoring capability or its
face image inclusion capability.  If you would like to include face
images in email, you'll also need to install the faces-xface package.  If
you would like to develop xface applications, you'll need to also install
faces-devel.

%package xface
Requires:	libgr-progs
Summary:	Utilities needed by mailers for handling Faces' X-face images.
Group:		Applications/Mail

%description xface
Faces-xface includes the utilities that mail user agent programs need to
handle X-Face mail headers.  When an email program reads the X-face
header line in an email message, it calls these utilities to display
the face image included in the message.

You'll need to install faces-xface if you want your mail program to
display Faces' X-face images.

%package devel
Summary:	The Faces program's library and header files.
Group:		Development/Libraries

%description devel
Faces-devel contains the faces program development environment,
(i.e., the static libraries and header files).

If you want to develop Faces applications, you'll need to install
faces-devel.  You'll also need to install the faces package.

%prep
%setup -q -n faces
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" -f Makefile.dist x11

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir}/faces,%{_mandir}/man{1,3}}

make -f Makefile.dist \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	install

install compface/compface.h $RPM_BUILD_ROOT%{_includedir}/compface.h

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/* || :

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man{1,3}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
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
%{_mandir}/man1/faces.1.gz
%{_mandir}/man1/face_update.1.gz
%{_mandir}/man1/compface.1.gz
%{_mandir}/man3/compface.3.gz

%files xface
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uncompface
%attr(755,root,root) %{_bindir}/ikon2xbm
%{_mandir}/man1/uncompface.1.gz
%{_mandir}/man3/uncompface.3.gz

%files devel
%defattr(644,root,root,755)
%{_includedir}/compface.h
%{_libdir}/libcompface.a
