INKSCAPE ?= /usr/bin/inkscape
illustrations_dir := figures/illustrations
illustrations_svgs := $(wildcard $(illustrations_dir)/*.svg)
illustrations_pdfs := $(patsubst %.svg,%.pdf,$(illustrations_svgs))

results_dir := figures/results

export PYTHONPATH := $(CURDIR)/results/code
export MATPLOTLIBRC := $(CURDIR)/results

.PHONY: all illustrations results

all: illustrations results

illustrations: $(illustrations_pdfs)
	@echo '********Generating illustrations********'
	@echo $(illustrations_svgs)
	@echo $(illustrations_pdfs)

$(illustrations_pdfs): $(illustrations_svgs)
	@$(INKSCAPE) -z --file=$<  --export-pdf=$@ --export-ignore-filters

results:
	$(MAKE) --no-print-directory -C results
