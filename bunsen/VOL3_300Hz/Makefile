.PHONY: flame_detection
flame_detection:
	mkdir -p inout.d
	mkdir -p input.d
	mkdir -p output.d
	mkdir -p visualisation.ref

.PHONY: video
video:
	ffmpeg -r 10 -i inout.d/pinchOff-%d.png -c:v libx264 -pix_fmt yuv420p inout.mp4
	ffmpeg -r 10 -i input.d/pinchOff-%d.png -c:v libx264 -pix_fmt yuv420p input.mp4
	ffmpeg -r 10 -i output.d/pinchOff-%d.png -c:v libx264 -pix_fmt yuv420p output.mp4

.PHONY: ref
ref:
	mkdir -p ref
	python3 phase.py

.PHONY: clean
clean:
	-rm -r inout.d
	-rm -r input.d
	-rm -r output.d
	-rm -r ref
	-rm -r visualisation.ref
	-rm inout.mp4
	-rm input.mp4
	-rm output.mp4
