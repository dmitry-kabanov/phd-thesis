inkscape ?= /usr/bin/inkscape
illustrations_path = figures/illustrations
svgs = $(wildcard $(illustrations_path)/*.svg)
pdfs = $(patsubst %.svg,%.pdf,$(svgs))

.PHONY: all
all: illustrations

.PHONY: illustrations
illustrations: $(pdfs)

$(illustrations_path)/%.pdf: $(illustrations_path)/%.svg
	$(inkscape) -z --file=$<  --export-pdf=$@ --export-ignore-filters

