# SPDX-License-Identifqier: MIT
%global forgeurl https://github.com/mitradranirban/font-uniol
Version:   1.0.1
Release:   6%{?dist}
%forgemeta
URL: %{forgeurl}
%global fontfamily    uniol        
%global fontlicense       OFL
%global fontlicenses      LICENCE
%global fontdocs       README.md   
%global fontdocsex        %{fontlicenses}
%global fontsummary       Unicode compliant Open source Ol Chiki font
%global fonts            *.ttf
%global fontconfs        66-0-%{fontpkgname}.conf
BuildRequires: fontforge 

%global fontdescription  %{expand:
 This is an Unicode compliant OlChiki or OlCemet font.
 OlChiki is a modern alphabetic script used to write Santhali 
 language used in various states of India. 
}

Source0: %{forgesource}

%fontpkg 

%prep
%forgesetup
chmod 755 generate.pe
./generate.pe *.sfd

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
*  Sun Feb 06 2022 11:35:37 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  1.0.1-6
- corrected disttag
* Sun Feb 06 2022 11:35:37 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  1.0.1-5
- reset forgemeta after adjusting 

* Sun Feb 06 2022 05:35:37 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  1.0.1-4
- Removed forgemeta and make standard git source setup

* Sat Feb 05 2022 22:30:36 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  1.0.1-2
- setup %%forgemeta before %%forgesource

* Sat Feb 05 2022 21:50:48 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  1.0.1-1
- upstream version bumped to 1.0.1 
- fontconfig files and ttf generation script added to source
- removed reference to Source1 and Source2 in spec file as they are merged into upstream

* Sat Feb 05 2022 18:50:28 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  1.0.0-4
- added copy command for Source2 and Source3
- corrected typo for forgesource

* Sat Feb 05 2022 16:50:14 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  1.0.0-3
- changed tag to 1.0.0
- added %%forgemacro 

* Sat Feb 05 2022 14:10:14 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  1.0.0-2
- changed to forgesetup from forgeurl 
- modified dtd line in fontconfig 

* Thu Feb 03 2022 20:56:29 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  1.0.0-1
- First relase 
