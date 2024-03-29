var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var nrOfParticipants = 1;
jQuery(function () {
    armPage('about');
    armPage('work');
    armPage('education');
    armPage('skills');
    armPage('music');
    armPage('email');
    setStars();
    addPraticipant();
    removeParticipant();
    $('textarea').on('input', function () {
        $(this).height("");
        var scrollHeight = $(this).prop('scrollHeight');
        $(this).height(scrollHeight);
    });
    $('.nav-item').on('click', handleMenu);
    $('.hamburger').on('click', handleMenu);
    window.onpopstate = function () {
        var id = window.location.pathname;
        if (id === '/') {
            id = 'about';
        }
        else {
            id = id.replace(/\//g, '');
        }
        renderPage(id, true);
    };
});
function renderPage(elemId, back) {
    if (back === void 0) { back = false; }
    return __awaiter(this, void 0, void 0, function () {
        var titles, data, url, response, e_1, key;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    titles = {
                        about: 'Um Mig',
                        work: 'Reynsla',
                        education: 'Menntun',
                        skills: 'Hæfni',
                        music: 'Tónlist',
                        email: 'Hafa Samband'
                    };
                    url = "/".concat(elemId, "-tag/");
                    _a.label = 1;
                case 1:
                    _a.trys.push([1, 4, , 5]);
                    return [4, fetch(url)];
                case 2:
                    response = _a.sent();
                    if (!response.ok) {
                        throw new Error("Result not ok");
                    }
                    return [4, response.text()];
                case 3:
                    data = _a.sent();
                    return [3, 5];
                case 4:
                    e_1 = _a.sent();
                    console.warn('Unable to fetch data', e_1);
                    data = null;
                    return [3, 5];
                case 5:
                    if (data) {
                        key = elemId;
                        $('title').html(titles[key]);
                        $(".grid-container").html(data);
                        $("html").animate({
                            scrollTop: 0
                        }, 1000);
                        if (!back)
                            window.history.pushState('', '', "/".concat(elemId, "/"));
                        if (elemId == 'skills')
                            setStars();
                    }
                    return [2];
            }
        });
    });
}
function armPage(elemId) {
    var elem = $("#".concat(elemId));
    elem.on("click", function () {
        renderPage(elemId);
    });
}
function addPraticipant() {
    $('#add-name').on("click", function () {
        nrOfParticipants++;
        var inputList = $('.name-inputs');
        var inputDiv = $('<div>');
        var nameInput = $('<input>');
        var mailInput = $('<input>');
        nameInput.attr({
            type: 'text',
            id: "name".concat(nrOfParticipants),
            name: "name".concat(nrOfParticipants),
            placeholder: "Nafn ".concat(nrOfParticipants)
        });
        mailInput.attr({
            type: 'email',
            id: "mail".concat(nrOfParticipants),
            name: "mail".concat(nrOfParticipants),
            placeholder: "Email ".concat(nrOfParticipants)
        });
        inputDiv.append(nameInput, mailInput, $('<br>'));
        inputList.append(inputDiv);
        $('#remove-name').prop('disabled', false);
    });
}
function removeParticipant() {
    $('#remove-name').on("click", function () {
        if (nrOfParticipants > 1) {
            $('.name-inputs').children().last().remove();
            nrOfParticipants--;
            if (nrOfParticipants <= 1) {
                $('#remove-name').prop('disabled', true);
            }
        }
    });
}
function setStars() {
    $('.stars').each(function () {
        var level = Number($(this).attr('level'));
        var index = 0;
        $(this).children().each(function () {
            if (index < level) {
                $(this).removeClass('star-empty');
                $(this).addClass('star-full');
                index++;
            }
        });
    });
}
function handleMenu() {
    var nav = $('nav');
    if (nav.hasClass('showMenu')) {
        nav.removeClass('showMenu');
        $('.closeIcon').css('display', 'none');
        $('.menuIcon').css('display', 'block');
    }
    else {
        nav.addClass('showMenu');
        $('.closeIcon').css('display', 'block');
        $('.menuIcon').css('display', 'none');
    }
}
//# sourceMappingURL=ajax.js.map