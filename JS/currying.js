//currying practice with strings and numbers

//add 5 to whichever number
var curriedAdder = function (a){
    return function(b) {
        return a + b;
    };
};

var byFive = curriedAdder(5);

console.log(byFive(1)); //returns 6
console.log(byFive(6)); //returns 11

//attach greeting, emphasis, and syntax to name
var greetDeeplyCurried = function(greeting) {
    return function(separator) {
        return function(emphasis) {
            return function(name) {
                console.log(greeting + separator + name + emphasis);
            };
        };
    };
};

var greetAwkwardly = greetDeeplyCurried("Hello")("...")("?");
greetAwkwardly("Heidi");//"Hello...Heidi?"

var sayHello = greetDeeplyCurried("Hello")(", ");
sayHello(".")("Heidi");//"Hello, Heidi."

var askHello = sayHello("?");
askHello("Heidi");//"Hello, Heidi?"

//greets by language
var curriedLang = function(greetingLang){
    return function(separatorLang){
        return function(emphasisLang){
            return function(nameLang){
                console.log(greetingLang + separatorLang + nameLang + emphasisLang);
            };
        };
    };
};

var greetFrench = curriedLang("Bonjour");
var awkwardFrench = greetFrench("...")("?");
awkwardFrench("Heidi");