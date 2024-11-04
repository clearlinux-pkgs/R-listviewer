#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-listviewer
Version  : 4.0.0
Release  : 44
URL      : https://cran.r-project.org/src/contrib/listviewer_4.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/listviewer_4.0.0.tar.gz
Summary  : 'htmlwidget' for Interactive Views of R Lists
Group    : Development/Tools
License  : MIT
Requires: R-listviewer-license = %{version}-%{release}
Requires: R-htmltools
Requires: R-htmlwidgets
Requires: R-shiny
BuildRequires : R-htmltools
BuildRequires : R-htmlwidgets
BuildRequires : R-reactR
BuildRequires : R-shiny
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
visualize or represent. Sometimes 'str()' is not enough, so this suite of
    htmlwidgets is designed to help see, understand, and maybe even modify your R
    lists.  The function 'reactjson()' requires a package

%package license
Summary: license components for the R-listviewer package.
Group: Default

%description license
license components for the R-listviewer package.


%prep
%setup -q -n listviewer
pushd ..
cp -a listviewer buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1696264812

%install
export SOURCE_DATE_EPOCH=1696264812
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-listviewer
cp %{_builddir}/listviewer/inst/htmlwidgets/core-js/LICENSE %{buildroot}/usr/share/package-licenses/R-listviewer/49661ee31dd26cc528c1945ba413af3a0140505e || :
cp %{_builddir}/listviewer/inst/htmlwidgets/reactjson/LICENSE %{buildroot}/usr/share/package-licenses/R-listviewer/3a6db07370ae58ecd9449480fce405a62a0b6caa || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/listviewer/DESCRIPTION
/usr/lib64/R/library/listviewer/INDEX
/usr/lib64/R/library/listviewer/LICENSE
/usr/lib64/R/library/listviewer/Meta/Rd.rds
/usr/lib64/R/library/listviewer/Meta/features.rds
/usr/lib64/R/library/listviewer/Meta/hsearch.rds
/usr/lib64/R/library/listviewer/Meta/links.rds
/usr/lib64/R/library/listviewer/Meta/nsInfo.rds
/usr/lib64/R/library/listviewer/Meta/package.rds
/usr/lib64/R/library/listviewer/NAMESPACE
/usr/lib64/R/library/listviewer/NEWS.md
/usr/lib64/R/library/listviewer/R/listviewer
/usr/lib64/R/library/listviewer/R/listviewer.rdb
/usr/lib64/R/library/listviewer/R/listviewer.rdx
/usr/lib64/R/library/listviewer/examples/examples_gadget.R
/usr/lib64/R/library/listviewer/examples/examples_reactjson.R
/usr/lib64/R/library/listviewer/help/AnIndex
/usr/lib64/R/library/listviewer/help/aliases.rds
/usr/lib64/R/library/listviewer/help/listviewer.rdb
/usr/lib64/R/library/listviewer/help/listviewer.rdx
/usr/lib64/R/library/listviewer/help/paths.rds
/usr/lib64/R/library/listviewer/html/00Index.html
/usr/lib64/R/library/listviewer/html/R.css
/usr/lib64/R/library/listviewer/htmlwidgets/core-js/LICENSE
/usr/lib64/R/library/listviewer/htmlwidgets/core-js/dist/shim.min.js
/usr/lib64/R/library/listviewer/htmlwidgets/core-js/package.json
/usr/lib64/R/library/listviewer/htmlwidgets/jsonedit.js
/usr/lib64/R/library/listviewer/htmlwidgets/jsonedit.yaml
/usr/lib64/R/library/listviewer/htmlwidgets/jsoneditor/LICENSE.md
/usr/lib64/R/library/listviewer/htmlwidgets/jsoneditor/README.md
/usr/lib64/R/library/listviewer/htmlwidgets/jsoneditor/dist/jsoneditor.min.js
/usr/lib64/R/library/listviewer/htmlwidgets/jsoneditor/package.json
/usr/lib64/R/library/listviewer/htmlwidgets/reactjson.js
/usr/lib64/R/library/listviewer/htmlwidgets/reactjson.yaml
/usr/lib64/R/library/listviewer/htmlwidgets/reactjson/LICENSE
/usr/lib64/R/library/listviewer/htmlwidgets/reactjson/README.md
/usr/lib64/R/library/listviewer/htmlwidgets/reactjson/dist/main.js
/usr/lib64/R/library/listviewer/htmlwidgets/reactjson/package.json
/usr/lib64/R/library/listviewer/rstudio/addins.dcf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-listviewer/3a6db07370ae58ecd9449480fce405a62a0b6caa
/usr/share/package-licenses/R-listviewer/49661ee31dd26cc528c1945ba413af3a0140505e
