Summary: GNOME network information applet
Name: gnome-netstatus
Version: 2.26.0
Release: %mkrel 1
License: GPLv2+
Group: Graphical desktop/GNOME
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0: gnome-netstatus-2.26.0-fix-str-fmt.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libpanel-applet-devel
BuildRequires: libglade2.0-devel
BuildRequires: gtk+2-devel >= 2.3.1
BuildRequires: scrollkeeper
BuildRequires: gnome-doc-utils
BuildRequires: libxslt-proc
BuildRequires: intltool
Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
This package contains an applet which provides information
about a network interface on your panel.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std _ENABLE_SK=false
%find_lang %{name} --with-gnome
for omf in %buildroot%_datadir/omf/%name/%name-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/%name-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done
rm -rf %buildroot/var/lib/scrollkeeper

%clean
rm -rf $RPM_BUILD_ROOT

%post
%post_install_gconf_schemas netstatus
%update_scrollkeeper
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas netstatus

%postun
%clean_scrollkeeper
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README TODO ChangeLog AUTHORS NEWS
%{_sysconfdir}/gconf/schemas/*
%{_libdir}/gnome-netstatus-applet
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/gnome-netstatus
%dir %{_datadir}/omf/%name
%dir %{_datadir}/omf/%name/%name-C.omf
%_datadir/icons/hicolor/48x48/apps/gnome-netstatus*


