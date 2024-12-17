let fields = document.querySelectorAll('form input');
console.log(fields);
try {
    document.querySelector('form #id_username').setAttribute('placeholder', 'Username');
    document.querySelector('form #id_password').setAttribute('placeholder', 'Password');
    document.querySelector('form #id_password1').setAttribute('placeholder', 'Password');
    document.querySelector('form #id_password2').setAttribute('placeholder', 'Confirm Password');
} catch {
    console.log(":(");
}
for (i = 0; i < fields.length; i++) {
    fields[i].classList.add('editText');

    //fields[i].setAttribute('placeholder', 'Username');
}
let spans = document.querySelectorAll('form span, label');
for (i = 0; i < spans.length; i++) {
    spans[i].style.display = "none";
}

let conditions = document.querySelectorAll('li');
for (i = 0; i < conditions.length; i++) {
    conditions[i].classList.add('conditions');
}

let errorslist = document.querySelector('.errorlist');
let errorlistChildren = errorslist.childNodes;
console.log(errorlistChildren);
for (i = 0; i < errorlistChildren.length; i++) {
    errorlistChildren[i].classList.add("error");
}