anychart.onDocumentReady(function() {
	var data = [

// Place exported content in data.txt between these two lines:
// ===================================================

{"x": "computer", "value": 3},{"x": "programmer", "value": 42},{"x": "new", "value": 16},{"x": "icde", "value": 14},{"x": "monthly", "value": 7},{"x": "newsletter", "value": 7},{"x": "gt", "value": 7},{"x": "subscribe", "value": 7},{"x": "programming", "value": 21},{"x": "coding", "value": 18},{"x": "hacking", "value": 13},{"x": "coder", "value": 9},{"x": "webdev", "value": 7},{"x": "nepdeveloper", "value": 8},{"x": "day", "value": 8},{"x": "daysofcode", "value": 9},{"x": "started", "value": 9},{"x": "app", "value": 9},{"x": "tracker", "value": 9},{"x": "connected", "value": 9},{"x": "api", "value": 9},{"x": "created", "value": 9},{"x": "signup", "value": 9},{"x": "screensrt", "value": 7},{"x": "dart", "value": 4},{"x": "see", "value": 4},{"x": "systemsofttech", "value": 7},{"x": "methods", "value": 4},{"x": "faster", "value": 4},{"x": "mastery", "value": 4},{"x": "productivity", "value": 4},{"x": "developer", "value": 11},{"x": "java", "value": 5},{"x": "functional", "value": 4},{"x": "python", "value": 7},{"x": "webdesign", "value": 9},{"x": "webdevelopment", "value": 9},{"x": "webdeveloper", "value": 9},{"x": "via", "value": 8},{"x": "iphonegalaxymd", "value": 6},{"x": "adding", "value": 5},{"x": "feature", "value": 6},{"x": "existing", "value": 6},{"x": "code", "value": 11},{"x": "linux", "value": 6},{"x": "kalilinux", "value": 6},{"x": "linuxmint", "value": 6},{"x": "cisco", "value": 6},{"x": "hacksquat", "value": 6},{"x": "hack", "value": 6},{"x": "hacker", "value": 6},{"x": "hacksrt", "value": 4},{"x": "job", "value": 8},{"x": "project", "value": 3},{"x": "nigelbpeck", "value": 3},{"x": "writing", "value": 3},{"x": "people", "value": 4},{"x": "time", "value": 4},{"x": "really", "value": 3},{"x": "lot", "value": 4},{"x": "land", "value": 4},{"x": "geneelvie", "value": 3},{"x": "understands", "value": 3},{"x": "hard", "value": 3},{"x": "democrats", "value": 3},{"x": "think", "value": 3},{"x": "youre", "value": 4},{"x": "stupid", "value": 3},{"x": "understand", "value": 3},{"x": "without", "value": 3},{"x": "experience", "value": 3},{"x": "freecodecamp", "value": 3}

// ===================================================

	];

	var chart = anychart.tagCloud(data);
	chart.title('KeyCloud Word Cloud Builder')
	chart.angles([0])
	chart.container("container");
	chart.draw();
});