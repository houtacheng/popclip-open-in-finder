// Clean the path from surrounding quotes, brackets, file:// prefix, escaped spaces, etc.
function cleanPath(raw) {
  if (!raw) return "";
  let p = raw.trim();

  // Strip enclosing quotes, brackets, and markdown wrappers
  const stripStart = /^["'`<\[(«“”‘]+/;
  const stripEnd = /["'`>\])»“”’]+$/;
  while (stripStart.test(p) || stripEnd.test(p)) {
    p = p.replace(stripStart, "").replace(stripEnd, "").trim();
  }

  // Handle file:// URIs
  if (p.startsWith("file://")) {
    p = decodeURI(p.slice(7));
  } else if (p.includes("%")) {
    try {
      p = decodeURI(p);
    } catch (e) {
      // ignore decoding error
    }
  }

  // Handle shell-escaped spaces (e.g. \ )
  p = p.replace(/\\ /g, " ");

  // Strip trailing punctuation if accidentally selected (e.g. at end of sentence)
  if (/[.,;:!?]$/.test(p) && p.length > 2 && !p.endsWith("/.")) {
    p = p.replace(/[.,;:!?]+$/, "");
  }

  return p.trim();
}

if (typeof popclip !== "undefined") {
  const rawText = (popclip.input.matchedText || popclip.input.text || "").trim();
  const targetPath = cleanPath(rawText);

  if (targetPath) {
    if (popclip.modifiers.option) {
      // Option + Click: Copy clean path to clipboard
      popclip.copyText(targetPath);
      popclip.showSuccess();
    } else {
      // Standard Click: Reveal file or folder in Finder
      try {
        popclip.revealFile(targetPath);
      } catch (error) {
        popclip.showText("❌ " + (error && error.message ? error.message : "Path not found"));
      }
    }
  }
}

if (typeof module !== "undefined") {
  module.exports = { cleanPath };
}
