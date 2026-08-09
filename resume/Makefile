PDF = rahul_resume.pdf
TEX = rahul_resume.tex

.PHONY: all clean

all: $(PDF)

$(PDF): $(TEX)
	tectonic $(TEX)

clean:
	rm -f rahul_resume.aux rahul_resume.log rahul_resume.out $(PDF)
