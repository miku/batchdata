Slides.pdf: Slides.md
	touch Slides.pdf && osascript marp.scpt
	# pandoc -t beamer $< -o $@

clean:
	rm -rf build/
	rm -rf dist/
	rm -f Slides.pdf
	find . -type d -name "__pycache__" -exec rm -rf {} \;

