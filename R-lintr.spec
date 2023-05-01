#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lintr
Version  : 3.0.2
Release  : 35
URL      : https://cran.r-project.org/src/contrib/lintr_3.0.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lintr_3.0.2.tar.gz
Summary  : A 'Linter' for R Code
Group    : Development/Tools
License  : MIT
Requires: R-backports
Requires: R-crayon
Requires: R-cyclocomp
Requires: R-digest
Requires: R-glue
Requires: R-jsonlite
Requires: R-knitr
Requires: R-rex
Requires: R-xml2
Requires: R-xmlparsedata
BuildRequires : R-backports
BuildRequires : R-crayon
BuildRequires : R-cyclocomp
BuildRequires : R-digest
BuildRequires : R-glue
BuildRequires : R-jsonlite
BuildRequires : R-knitr
BuildRequires : R-rex
BuildRequires : R-xml2
BuildRequires : R-xmlparsedata
BuildRequires : buildreq-R

%description
semantic issues.  Supports on the fly checking of R code edited with
    'RStudio IDE', 'Emacs', 'Vim', 'Sublime Text', 'Atom' and 'Visual
    Studio Code'.

%prep
%setup -q -n lintr
cd %{_builddir}/lintr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666195541

%install
export SOURCE_DATE_EPOCH=1666195541
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
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


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lintr/DESCRIPTION
/usr/lib64/R/library/lintr/INDEX
/usr/lib64/R/library/lintr/LICENSE
/usr/lib64/R/library/lintr/Meta/Rd.rds
/usr/lib64/R/library/lintr/Meta/features.rds
/usr/lib64/R/library/lintr/Meta/hsearch.rds
/usr/lib64/R/library/lintr/Meta/links.rds
/usr/lib64/R/library/lintr/Meta/nsInfo.rds
/usr/lib64/R/library/lintr/Meta/package.rds
/usr/lib64/R/library/lintr/Meta/vignette.rds
/usr/lib64/R/library/lintr/NAMESPACE
/usr/lib64/R/library/lintr/NEWS.md
/usr/lib64/R/library/lintr/R/lintr
/usr/lib64/R/library/lintr/R/lintr.rdb
/usr/lib64/R/library/lintr/R/lintr.rdx
/usr/lib64/R/library/lintr/doc/continuous-integration.R
/usr/lib64/R/library/lintr/doc/continuous-integration.Rmd
/usr/lib64/R/library/lintr/doc/continuous-integration.html
/usr/lib64/R/library/lintr/doc/creating_linters.Rmd
/usr/lib64/R/library/lintr/doc/creating_linters.html
/usr/lib64/R/library/lintr/doc/editors.R
/usr/lib64/R/library/lintr/doc/editors.Rmd
/usr/lib64/R/library/lintr/doc/editors.html
/usr/lib64/R/library/lintr/doc/index.html
/usr/lib64/R/library/lintr/doc/lintr.R
/usr/lib64/R/library/lintr/doc/lintr.Rmd
/usr/lib64/R/library/lintr/doc/lintr.html
/usr/lib64/R/library/lintr/example/bad.R
/usr/lib64/R/library/lintr/example/complexity.R
/usr/lib64/R/library/lintr/help/AnIndex
/usr/lib64/R/library/lintr/help/aliases.rds
/usr/lib64/R/library/lintr/help/lintr.rdb
/usr/lib64/R/library/lintr/help/lintr.rdx
/usr/lib64/R/library/lintr/help/paths.rds
/usr/lib64/R/library/lintr/html/00Index.html
/usr/lib64/R/library/lintr/html/R.css
/usr/lib64/R/library/lintr/lintr/linters.csv
/usr/lib64/R/library/lintr/rstudio/addins.dcf
/usr/lib64/R/library/lintr/syntastic/lintr.vim
/usr/lib64/R/library/lintr/tests/testthat.R
/usr/lib64/R/library/lintr/tests/testthat/checkstyle.xml
/usr/lib64/R/library/lintr/tests/testthat/default_linter_testcode.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/assignmentLinter/DESCRIPTION
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/assignmentLinter/NAMESPACE
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/assignmentLinter/R/abc.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/assignmentLinter/R/jkl.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/clean/DESCRIPTION
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/clean/NAMESPACE
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/clean/R/clean_generics.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/clean/R/default_linter_testcode.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/clean/lintr_test_config
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/clean_subdir/lintr_test_config
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/clean_subdir/r/DESCRIPTION
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/clean_subdir/r/NAMESPACE
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/clean_subdir/r/R/default_linter_testcode.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/clean_subdir/r/R/imported_methods.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/cp1252/DESCRIPTION
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/cp1252/NAMESPACE
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/cp1252/R/cp1252.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/cp1252/cp1252.Rproj
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/desc_dir_pkg/DESCRIPTION/R/foo.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/missing_dep/DESCRIPTION
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/missing_dep/NAMESPACE
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/missing_dep/R/foo.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/no_export_dep/DESCRIPTION
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/no_export_dep/NAMESPACE
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/no_export_dep/R/foo.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/package/DESCRIPTION
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/package/NAMESPACE
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/package/R/default_linter_testcode.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/package/data-raw/default_linter_testcode.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/package/inst/data-raw/default_linter_testcode.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/package/lintr_test_config
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/package/package.Rproj
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/package/vignettes/test.Rhtml
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/package/vignettes/test.Rmd
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/package/vignettes/test.Rnw
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/package/vignettes/test.Rrst
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/package/vignettes/test.Rtex
/usr/lib64/R/library/lintr/tests/testthat/dummy_packages/package/vignettes/test.Rtxt
/usr/lib64/R/library/lintr/tests/testthat/dummy_projects/project/cp1252.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_projects/project/cp1252_parseable.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_projects/project/default_linter_testcode.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_projects/project/mismatched_starts_ends.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_projects/project/one_start_no_end.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_projects/project/partially_matched_exclusions.R
/usr/lib64/R/library/lintr/tests/testthat/dummy_projects/project/project.Rproj
/usr/lib64/R/library/lintr/tests/testthat/exclusions-test
/usr/lib64/R/library/lintr/tests/testthat/helper.R
/usr/lib64/R/library/lintr/tests/testthat/knitr_formats/test.Rhtml
/usr/lib64/R/library/lintr/tests/testthat/knitr_formats/test.Rmd
/usr/lib64/R/library/lintr/tests/testthat/knitr_formats/test.Rnw
/usr/lib64/R/library/lintr/tests/testthat/knitr_formats/test.Rrst
/usr/lib64/R/library/lintr/tests/testthat/knitr_formats/test.Rtex
/usr/lib64/R/library/lintr/tests/testthat/knitr_formats/test.Rtxt
/usr/lib64/R/library/lintr/tests/testthat/knitr_malformed/incomplete_r_block.Rmd
/usr/lib64/R/library/lintr/tests/testthat/lints
/usr/lib64/R/library/lintr/tests/testthat/test-T_and_F_symbol_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-absolute_path_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-any_duplicated_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-any_is_na_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-assignment_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-backport_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-brace_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-cache.R
/usr/lib64/R/library/lintr/tests/testthat/test-checkstyle_output.R
/usr/lib64/R/library/lintr/tests/testthat/test-ci.R
/usr/lib64/R/library/lintr/tests/testthat/test-class_equals_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-closed_curly_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-commas_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-commented_code_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-comments.R
/usr/lib64/R/library/lintr/tests/testthat/test-condition_message_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-conjunct_test_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-consecutive_stopifnot_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-cyclocomp_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-defaults.R
/usr/lib64/R/library/lintr/tests/testthat/test-dir_linters.R
/usr/lib64/R/library/lintr/tests/testthat/test-duplicate_argument_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-equals_na_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-error.R
/usr/lib64/R/library/lintr/tests/testthat/test-exclusions.R
/usr/lib64/R/library/lintr/tests/testthat/test-expect_comparison_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-expect_identical_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-expect_length_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-expect_lint.R
/usr/lib64/R/library/lintr/tests/testthat/test-expect_named_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-expect_not_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-expect_null_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-expect_s3_class_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-expect_true_false_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-expect_type_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-extraction_operator_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-fixed_regex_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-function_argument_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-function_left_parentheses_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-get_source_expressions.R
/usr/lib64/R/library/lintr/tests/testthat/test-ids_with_token.R
/usr/lib64/R/library/lintr/tests/testthat/test-ifelse_censor_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-implicit_integer_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-infix_spaces_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-inner_combine_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-is_lint_level.R
/usr/lib64/R/library/lintr/tests/testthat/test-knitr_formats.R
/usr/lib64/R/library/lintr/tests/testthat/test-line_length_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-lint_file.R
/usr/lib64/R/library/lintr/tests/testthat/test-lint_package.R
/usr/lib64/R/library/lintr/tests/testthat/test-linter_tags.R
/usr/lib64/R/library/lintr/tests/testthat/test-literal_coercion_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-make_linter_from_regex.R
/usr/lib64/R/library/lintr/tests/testthat/test-methods.R
/usr/lib64/R/library/lintr/tests/testthat/test-missing_argument_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-missing_package_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-namespace.R
/usr/lib64/R/library/lintr/tests/testthat/test-namespace_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-nested_ifelse_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-no_tab_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-nonportable_path_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-normalize_exclusions.R
/usr/lib64/R/library/lintr/tests/testthat/test-numeric_leading_zero_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-object_length_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-object_name_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-object_usage_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-open_curly_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-outer_negation_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-package_hooks_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-paren_body_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-paren_brace_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-parse_exclusions.R
/usr/lib64/R/library/lintr/tests/testthat/test-paste_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-pipe_call_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-pipe_continuation_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-redundant_ifelse_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-regex_subset_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-rstudio_markers.R
/usr/lib64/R/library/lintr/tests/testthat/test-semicolon_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-seq_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-settings.R
/usr/lib64/R/library/lintr/tests/testthat/test-single_quotes_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-spaces_inside_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-spaces_left_parentheses_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-sprintf_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-string_boundary_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-strings_as_factors_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-system_file_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-todo_comment_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-trailing_blank_lines_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-trailing_whitespace_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-undesirable_function_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-undesirable_operator_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-unneeded_concatenation_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-unreachable_code_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-unused_import_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-use_lintr.R
/usr/lib64/R/library/lintr/tests/testthat/test-vector_logic_linter.R
/usr/lib64/R/library/lintr/tests/testthat/test-with.R
/usr/lib64/R/library/lintr/tests/testthat/test-with_id.R
/usr/lib64/R/library/lintr/tests/testthat/test-xml_nodes_to_lints.R
/usr/lib64/R/library/lintr/tests/testthat/test-yoda_test_linter.R
