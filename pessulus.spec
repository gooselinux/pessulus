%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define basever 2.28

Name:           pessulus
Version:        %{basever}.0
Release:        1%{?dist}
Summary:        A lockdown editor for GNOME

Group:          Applications/System
License:        GPLv2+
URL:            http://live.gnome.org/Pessulus
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{basever}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:	gtk2-devel
BuildRequires:  pygtk2-devel
BuildRequires:  gnome-python2-devel
BuildRequires:  GConf2-devel,
BuildRequires:  gnome-python2-gconf
BuildRequires:  gnome-python2-desktop
BuildRequires:  perl-XML-Parser
#BuildRequires:  pkgconfig
BuildRequires:  gettext-devel
BuildRequires:  intltool >= 0.35.0
BuildRequires:  desktop-file-utils
Requires:  gnome-python2-gconf
Requires:  gnome-python2-bugbuddy
Requires:  gnome-python2-desktop

%description
Pessulus is a lockdown editor for GNOME, written in python. Pessulus 
enables administrators to set mandatory settings in GConf. The 
users can not change these settings.
Use of pessulus can be useful on computers that are open to use by 
everyone, e.g. in an internet cafe.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
chmod +x $RPM_BUILD_ROOT%{python_sitelib}/Pessulus/*.py

desktop-file-install --vendor="" --delete-original --remove-category="System" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications        \
  $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README AUTHORS COPYING ChangeLog
%{_bindir}/%{name}
%{python_sitelib}/Pessulus/
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/pessulus.*

%changelog
* Sun Sep 25 2009 Haïkel Guémar <karlthered@gmail.com> - 2.28.0-1
- Updated to 2.28.0

* Mon Sep 14 2009 Haïkel Guémar <karlthered@gmail.com> - 2.27.92-1
- Updated to 2.27.92

* Wed Jul 29 2009 Haïkel Guémar <karlthered@gmail.com> - 2.27.5-1
- Updated to 2.24.0
- Remove now unneeded pythondir patch (GNOME #549728 fixed upstream)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.23.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.23.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.23.1-3
- Rebuild for Python 2.6

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.23.1-2
- fix missing BR, Requires

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.23.1-1
- fix license tag
- update to 2.23.1
- install into pythondir (not pyexecdir)

* Mon Apr 16 2007 Damien Durand <splinux@fedoraproject.org> - 2.16.2-2
- Fix desktop-file

* Fri Dec 22 2006 Damien Durand <splinux@fedoraproject.org> - 2.16.2-1
- Upgrade to 2.16.2
- Add gnome-python2-devel in BR

* Sat Sep 23 2006 Damien Durand <splinux@fedoraproject.org> - 2.16.1-1
- Upgrade to 2.16.1
- Fixe #195819

* Sat Sep 23 2006 Damien Durand <splinux@fedoraproject.org> - 2.16-4
- Bump release

* Wed Sep 06 2006 Damien Durand <splinux@fedoraproject.org> - 2.16.0-1
- Upgrade to 2.16 release
- Add gnome-python2-gconf in Requires

* Fri Aug 08 2006 Damien Durand <splinux@fedoraproject.org> - 2.15.91-2
- Bump release

* Fri Aug 08 2006 Damien Durand <splinux@fedoraproject.org> - 2.15.91-1
- Upgraded to 2.15.91

* Fri Jul 28 2006 Damien Durand <splinux@fedoraproject.org> - 2.15.90-1
- Fix URL
- Upgrad to 2.15.90

* Tue Jul 11 2006 Damien Durand <splinux@fedoraproject.org> - 0.10.4-1
- upgrad to 0.10.4

* Tue Jul 04 2006 Damien Durand <splinux@fedoraproject.org> - 0.10.1-3
- fix debuginfo packages

* Thu Jun 15 2006 Damien Durand <splinux@fedoraproject.org> - 0.10.1-2
- fix BuildRequires

* Wed May 3 2006 Damien Durand <splinux@fedoraproject.org> - 0.10.1-1
- upgrade version to 0.10.1

* Fri Apr 7 2006 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9-2
- fix BR
- remove unnecessary Requires
- use version-release in changelog entries
- fix directory ownership
- use python_sitearch
- make python "scripts" executable

* Thu Apr 6 2006 Damien Durand <splinux@fedoraproject.org> - 0.9-1
- Initial package
