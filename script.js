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
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
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
var VERIFICARBTN = document.getElementById('verificarbtn');
function gerarCharada() {
    return __awaiter(this, void 0, void 0, function () {
        var divexplica, explica, PERGUNTA, RESPOSTACAMPO, FORMULARIO, PALPITE, APIURL, RESPONSE, DADOS, error_1;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    PERGUNTA = document.getElementById('pergunta');
                    RESPOSTACAMPO = document.getElementById('resposta');
                    FORMULARIO = document.getElementById('formulario');
                    PALPITE = document.getElementById('palp');
                    explica = document.getElementById('explicacao');
                    divexplica = document.getElementById('divexplicacao');
                    APIURL = 'http://127.0.0.1:80/charadas';
                    _a.label = 1;
                case 1:
                    _a.trys.push([1, 4, , 5]);
                    return [4 /*yield*/, fetch(APIURL)];
                case 2:
                    RESPONSE = _a.sent();
                    return [4 /*yield*/, RESPONSE.json()];
                case 3:
                    DADOS = _a.sent();
                    PERGUNTA.innerHTML = DADOS.pergunta;
                    explica.innerText = DADOS.explicacao;
                    RESPOSTACAMPO.value = DADOS.resposta;
                    PALPITE.value = "";
                    FORMULARIO.style.display = "block";
                    divexplica.style.display = "none";
                    RESPOSTACAMPO.style.visibility = 'hidden';
                    VERIFICARBTN.disabled = false;
                    return [3 /*break*/, 5];
                case 4:
                    error_1 = _a.sent();
                    return [3 /*break*/, 5];
                case 5: return [2 /*return*/];
            }
        });
    });
}
function verificar() {
    var RESPOSTACAMPO = document.getElementById('resposta');
    var divexplica = document.getElementById('divexplicacao');
    var resposta = RESPOSTACAMPO.value;
    var PALPITE = document.getElementById('palp');
    if (PALPITE.value.trim() === "") {
        RESPOSTACAMPO.value = "N\u00E3o deixe o campo em branco!";
        RESPOSTACAMPO.style.visibility = 'visible';
        VERIFICARBTN.disabled = true;
    }
    else if (resposta[0] == (PALPITE.value)) { //Verifica se a palavra escrita está dentro da resposta
        RESPOSTACAMPO.value = "Parab\u00E9ns, voc\u00EA acertou. A resposta \u00E9: ".concat(resposta);
        RESPOSTACAMPO.style.visibility = 'visible';
        divexplica.style.display = 'block';
        VERIFICARBTN.disabled = true;
    }
    else {
        RESPOSTACAMPO.value = "Que pena, voc\u00EA errou. A resposta \u00E9: ".concat(resposta);
        RESPOSTACAMPO.style.visibility = 'visible';
        VERIFICARBTN.disabled = true;
        divexplica.style.display = 'block';
    }
}
(function () {
    'use strict';
    var FORMS = document.querySelectorAll('.needs-validation');
    Array.from(FORMS).forEach(function (form) {
        FORMS.addEventListener('submit', function (event) {
            if (FORMS.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            FORMS.classList.add('was-validated');
        }, false);
    });
})();