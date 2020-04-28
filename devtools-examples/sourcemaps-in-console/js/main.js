// Generated by CoffeeScript 1.10.0
(function() {
  var greet, greetButton, person;

  person = document.getElementById('person');

  greet = function(greeting) {
    return console.log(greeting + " " + person.value);
  };

  person.addEventListener("focus", function() {
    return person.value = "";
  });

  greetButton = document.getElementById('greet');

  greetButton.addEventListener("click", function() {
    var greeting, helloOption;
    helloOption = document.querySelector("#hello");
    greeting = helloOption.checked ? "Hello" : "Goodbye";
    return greet(greeting);
  });

}).call(this);

//# sourceMappingURL=main.js.map
