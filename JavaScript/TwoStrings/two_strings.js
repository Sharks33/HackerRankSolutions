process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function twoStrings(s1, s2){
    // Complete this function
    var setS1 = new Set(s1);
    var setS2 = new Set(s2);
    var hasSubStr = "NO"

    setS1 = Array.from(setS1);
    setS2 = Array.from(setS2);

    var arrayLength1 = setS1.length;
    var arrayLength2 = setS2.length;

    Array.prototype.contains = function ( needle ) {
       for (i in this) {
           if (this[i] === needle) return true;
       }
       return false;
    }

    for (var i = 0; i < arrayLength1; i++) {
        if (setS2.contains(setS1[i])) {
            hasSubStr = "YES"
        }
    }

    for (var j = 0; j < arrayLength2; j++) {
        if (setS1.contains(setS2[j])) {
            hasSubStr = "YES"
        }
    }

    return hasSubStr;

}

function main() {
    var q = parseInt(readLine());
    for(var a0 = 0; a0 < q; a0++){
        var s1 = readLine();
        var s2 = readLine();
        var result = twoStrings(s1, s2);
        process.stdout.write("" + result + "\n");
    }

}
