window.MathJax = {
    tex: {
        inlineMath: [["\\(", "\\)"]],
        displayMath: [["\\[", "\\]"]],
        processEscapes: true,
        processEnvironments: true
    },
    options: {
        ignoreHtmlClass: ".*|",
        processHtmlClass: "arithmatex"
    }
};

/* İşte sihirli dokunuş burası: Sayfa her değiştiğinde MathJax'i dürtüyoruz */
document$.subscribe(() => {
    MathJax.typesetPromise()
})