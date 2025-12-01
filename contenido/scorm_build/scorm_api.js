// scorm_api.js - Wrapper SCORM 1.2 muy sencillo

var ScormAPI = (function () {
    var api = null;
    var initialized = false;
    var finished = false;

    function findAPIInWindow(win) {
        var maxDepth = 10;
        var depth = 0;
        while (win && depth < maxDepth) {
            try {
                if (win.API) {
                    return win.API;
                }
            } catch (e) {}
            if (win.parent === win) {
                break;
            }
            win = win.parent;
            depth++;
        }
        return null;
    }

    function getAPIHandle() {
        if (api !== null) {
            return api;
        }
        api = findAPIInWindow(window);
        if (api === null && window.opener) {
            api = findAPIInWindow(window.opener);
        }
        return api;
    }

    function init() {
        if (initialized) return true;
        var theAPI = getAPIHandle();
        if (!theAPI || !theAPI.LMSInitialize) {
            console.warn("No se encontró API SCORM 1.2");
            return false;
        }
        var result = theAPI.LMSInitialize("");
        if (result === "true") {
            initialized = true;
            return true;
        } else {
            console.warn("LMSInitialize devolvió", result);
            return false;
        }
    }

    function finish() {
        if (!initialized || finished) return true;
        var theAPI = getAPIHandle();
        if (!theAPI || !theAPI.LMSFinish) return false;
        var result = theAPI.LMSFinish("");
        finished = (result === "true");
        return finished;
    }

    function setValue(element, value) {
        var theAPI = getAPIHandle();
        if (!theAPI || !theAPI.LMSSetValue) return false;
        var result = theAPI.LMSSetValue(element, value);
        return (result === "true");
    }

    function commit() {
        var theAPI = getAPIHandle();
        if (!theAPI || !theAPI.LMSCommit) return false;
        var result = theAPI.LMSCommit("");
        return (result === "true");
    }

    return {
        init: init,
        finish: finish,
        set: setValue,
        commit: commit
    };
})();
