%{?_javapackages_macros:%_javapackages_macros}

Name:          lzma-java
Version:       1.3
Release:       3.1
Summary:       LZMA library for Java
Group:         Development/Java
# Source files without license headers https://github.com/jponge/lzma-java/issues/13
# Public Domain: ./src/main/java/lzma/sdk/*  ./src/test/java/lzma/*
License:       ASL 2.0 and Public Domain
URL:           http://jponge.github.io/lzma-java/
Source0:       https://github.com/jponge/lzma-java/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
# ./src/main/java/lzma/ http://www.7-zip.org/sdk.html
Provides:      bundled(lzma-sdk-java) = 16.02
BuildArch:     noarch

%description
This library is based on the Java LZMA SDK by Igor Pavlov.
It brings many improvements, including Java conventions and
a Java I/O streaming API.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-release-plugin

%mvn_file com.github.jponge:%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 22 2016 gil cattaneo <puntogil@libero.it> 1.3-1
- initial rpm

