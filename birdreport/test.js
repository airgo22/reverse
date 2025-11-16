var cryptojs = require("crypto-js");
var JSEncrypt = require("jsencrypt") ;

function MD5(string) {
    return cryptojs.MD5(string).toString();
}

function getUuid() {
    var s = [];
    var hexDigits = "0123456789abcdef";
    for (var i = 0; i < 32; i++) {
        s[i] = hexDigits.substr(Math.floor(Math.random() * 16), 1)
    }
    s[14] = "4";
    s[19] = hexDigits.substr(s[19] & 3 | 8, 1);
    s[8] = s[13] = s[18] = s[23];
    var uuid = s.join("");
    return uuid
}

function get_data(page) {
    var timestamp = Date.parse(new Date);
    var requestId = getUuid();
    var data = `{"limit":"20","page":${page}}` // <- JSON.stringify(sort_ASCII(dataTojson(options.data || "{}")));
    var paramPublicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCvxXa98E1uWXnBzXkS2yHUfnBM6n3PCwLdfIox03T91joBvjtoDqiQ5x3tTOfpHs3LtiqMMEafls6b0YWtgB1dse1W5m+FpeusVkCOkQxB4SZDH6tuerIknnmB/Hsq5wgEkIvO5Pff9biig6AyoAkdWpSek/1/B7zYIepYY0lxKQIDAQAB";
    var encrypt = new JSEncrypt;
    encrypt.setPublicKey(paramPublicKey);
    load_data = encrypt.encrypt(data);
    var sign = MD5(data + requestId + timestamp);
    return {
        requestId: requestId,
        timestamp: timestamp,
        sign: sign,
        data: load_data
    } ;
}

function decode_data(data) { 
    var key = "C8EB5514AF5ADDB94B2207B08C66601C" ;
    var iv = "55DD79C6F04E1A67" ;
    decoded_data = cryptojs.AES.decrypt(data, cryptojs.enc.Utf8.parse(key), {
        iv: cryptojs.enc.Utf8.parse(iv),
        mode: cryptojs.mode.CBC,
        padding: cryptojs.pad.Pkcs7
    }) ;
    return decoded_data.toString(cryptojs.enc.Utf8) ;
}

console.log(get_data("1"));