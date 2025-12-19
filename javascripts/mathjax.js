window.MathJax = {
    tex: {
        // Hem $...$ hem \( ... \) destekli olsun
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']],
        processEscapes: true,
        processEnvironments: true
    },
    svg: {
        fontCache: 'global'
    }
};

// MkDocs Material sayfa içi gezinmelerde de yeniden render etsin
document$.subscribe(() => {
    MathJax.typesetPromise();
});