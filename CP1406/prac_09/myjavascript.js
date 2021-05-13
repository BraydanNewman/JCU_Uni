/*
let message = "Hello!";
alert(message);
message = "What is your name";
let userName = prompt(message);
alert("You said: " + userName);

if (userName.length < 5) {
    userName = prompt("Please enter a user name that has more than one letter.");
    alert("You said" + userName + "is more then one");
} else {
    alert("Your username was accepted on the first try!");
}

while (userName.length <= 0) {
    userName = prompt("Please enter a user name that has at least one letter.");
}
if (userName.length < 2) {
    alert("I see you are using an initial");
} else {
    alert("Your userName is now updated");
}
*/

function showMessage() {
    const d = new Date();
    let a = d.getTime();
    alert('Hello everyone!');
    alert('milliseconds since 1970 is: ' + a)
    confirm("Are you Sure")
}