Name: gnome-gmail
Version: 1.3
Release: 1
Group: Applications/Communications
Vendor: David Steele
URL: http://sourceforge.net/projects/%{name}
License: GPLv2
Summary: Make Gmail an option for the default Gnome mail handler
# source script is embedded in a blog post at:
# http://matthew.ruschmann.net/blog/Linux/gnome-gmail-1.1.html
Source: %{name}-%{version}.tgz
Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires: control-center
Requires: python
Requires: pygobject2

%description
This package makes Gmail a choice in the Gnome control panel for the default
mail handler. It opens in the default web browser.

%prep
%setup -q

%build

%install
rm -Rf %{buildroot}
install -D gnome-gmail %{buildroot}/usr/bin/gnome-gmail
install -D gnome-gmail.xml %{buildroot}/usr/share/gnome-control-center/default-apps/gnome-gmail.xml

%post

#export xmlfile="/usr/share/gnome-control-center/gnome-default-applications.xml"

#if [ -f /usr/share/gnome-control-center/default-apps/gnome-default-applications.xml ] 
#then
#	cp /usr/share/doc/gnome-gmail-1.2/gnome-gmail.xml /usr/share/gnome-control-center/default-apps/
#fi

#if [ -f $xmlfile ] && ! grep -q gnome-gmail $xmlfile 
#then
#sed -i -e 's/<mail-readers>/<mail-readers>\
#    <mail-reader>\
#      <name>Gmail<\/name>\
#      <executable>gnome-gmail<\/executable>\
#      <command>gnome-gmail \%s<\/command>\
#      <icon-name>redhat-email.png<\/icon-name>\
#      <run-in-terminal>false<\/run-in-terminal>\
#    <\/mail-reader>/' $xmlfile
#fi

%clean
rm -Rf %{buildroot}

%files
%doc README COPYING
%attr( 0755, root, root) /usr/bin/gnome-gmail
%attr( 0644, root, root) /usr/share/gnome-control-center/default-apps/gnome-gmail.xml

%changelog
* Mon Sep 07 2009 Dave Steele <daves@users.sourceforge.net> - 1.1-1
- initial package release

* Wed Sep 09 2009 Dave Steele <daves@users.sourceforge.net> - 1.2-1
- Better gmail URL
